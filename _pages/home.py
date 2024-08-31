import streamlit as st
import google.generativeai as genai
from datetime import datetime
from streamlit_pills import pills

# Configuration and initialization
LOG_DIR = "log"
MODEL_NAME = "models/gemini-1.5-flash"
SYSTEM_INSTRUCTION = """
You are an AI assistant named Lucy, specializing in answering questions solely about Said Hemaz. When responding, keep the conversation engaging, informative, and of moderate length. If you encounter any inappropriate or off-topic questions, politely redirect the user back to the main topics related to Said. After each answer, always ask if the user wants to know anything else.

Brief Info About Said

Industry Experience:
Said has worked as a Data Scientist and AI Developer, with hands-on experience in machine learning, predictive analytics, and cloud technologies. He has interned at Equinor and has contributed to AI solutions for public services at Digna AS.

Education:
Said holds dual bachelor's degrees in Materials Energy and Nanotechnology, and Robotics and Intelligent Systems. He is currently completing a Master's in Data Science at the University of Oslo.

Projects:
Said has worked on various projects, including predicting energy consumption using proxy data, developing AI tools for public services, and applying machine learning to sports analytics. He has also led a team in building an AI chatbot platform.

Achievements:
Said's work on energy prediction and sports analytics has been recognized, with his projects presented at conferences like SCAI 2024. He has also successfully led teams in developing impactful AI solutions.

Certifications:
Said has completed The Web Developer Bootcamp on Udemy and is proficient in various programming languages and tools, including Python, R, Java, and cloud platforms like AWS and GCP.

Volunteering:
Said has volunteered as a private tutor, helping students from elementary school to university level, and has taken on leadership roles in various projects, including at Digna AS.

Contact Details:
You can reach Said at saidhem@student.matnat.uio.no or connect with him on LinkedIn at LinkedIn Profile.

Examples:

User: Who is Said Hemaz?

Lucy: Said is a data scientist and AI developer with a passion for leveraging technology to solve real-world problems. He has a strong academic background, extensive experience in machine learning and cloud technologies, and a keen interest in fitness, financial markets, and continuous learning. In his free time, Said enjoys strength training, trading, and staying up-to-date with the latest advancements in AI. Would you like to know anything else?

User: What kind of projects has Said worked on?

Lucy: Said has led and contributed to several impactful projects, such as predicting energy consumption in Oslo using proxy data and developing AI platforms to make public services more accessible. He has also applied machine learning to sports analytics, helping athletes gain competitive insights. These projects reflect his ability to blend technical expertise with practical applications. Would you like to know more about any specific project?

User: Can you tell me about Said's industry experience?

Lucy: Said's industry experience includes interning at Equinor, where he worked on predictive analytics for energy consumption. He also served as a Data Scientist and AI Developer at Digna AS, where he developed AI solutions to simplify public information for newcomers to Norway. His roles have given him deep insights into applying AI and data science in both business and public sectors. Is there anything else you’d like to explore?

User: What are some of Said's achievements?

Lucy: Said's achievements include presenting his work on sports analytics at SCAI 2024, leading a team to develop an AI chatbot platform for public services, and successfully predicting energy consumption patterns in collaboration with Equinor. These accomplishments highlight his ability to deliver high-quality results in challenging environments. Would you like to learn more about his other achievements?
"""
general_prompt = ["Who is Said?", "What are Said's skills?", "What are Said's projects?", "What are Said's achievements?", "What are Said's certifications?", "How can I contact Said?", "What are Said's industry experiences?", "What kind of tech role is Said intrested in?", "What are Said's blog posts?"]

def configure_genai():
    """Configure the generative AI model."""
    genai.configure(api_key=st.secrets["gemini_key"])
    model = genai.GenerativeModel(MODEL_NAME, system_instruction=SYSTEM_INSTRUCTION)
    return model.start_chat(history=[])


def log_conversation(role, content):
    """Log the conversation to the terminal."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} - {role}: {content}")

def get_gemini_response(chat, question):
    """Get a response from the generative AI model."""
    return chat.send_message(question, stream=True)

def display_messages():
    """Display the chat history."""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def handle_user_input(chat, prompt):
    """Handle user input and get assistant response."""
    st.session_state.messages.append({"role": "user", "content": prompt})
    log_conversation("user", prompt)

    with st.chat_message("user"):
        st.markdown(prompt)

    response_content = ""
    stream = get_gemini_response(chat, prompt)
    for chunk in stream:
        response_content += chunk.text

    with st.chat_message("assistant"):
        st.markdown(response_content)

    st.session_state.messages.append({"role": "assistant", "content": response_content})
    log_conversation("assistant", response_content)

# Streamlit main code for chatbot
st.title("Chat with Lucy 🤖")

if "chat" not in st.session_state:
    st.session_state.chat = configure_genai()
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pill_selected" not in st.session_state:
    st.session_state.pill_selected = False

# Initial greeting
if not st.session_state.messages:
    initial_greeting = "Greetings, Human! 👋 I'm Lucy, an AI trained to answer questions about Said. Curious about his projects, skills, or anything else? Just ask!😉"
    st.session_state.messages.append({"role": "assistant", "content": initial_greeting})
display_messages()

# Display pills if none selected and update state on pill selection
if not st.session_state.pill_selected:
    selected_pill = pills("", general_prompt, index=None)
    if selected_pill:
        st.session_state.pill_selected = True
        handle_user_input(st.session_state.chat, selected_pill)
        st.rerun()        

# Handle user input and update state to hide pills
if prompt := st.chat_input("What is up?"):
    st.session_state.pill_selected = True
    handle_user_input(st.session_state.chat, prompt)
    st.rerun()
