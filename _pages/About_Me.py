# Define the left and right columns
right_column, left_column = st.columns([1, 2])
with right_column:
    st.markdown("<br>", unsafe_allow_html=True)
    st.image(r"images/profile.png", use_column_width=True)

with left_column:
    st.title("About Me")
    st.markdown(
        "<div style='text-align: justify'>"
        "Hello! I'm Said, I am a passionate Data Scientist and AI Developer with a strong foundation in machine learning, data analytics, and cloud technologies. With a dual bachelor's degree in Materials Energy and Nanotechnology, and Robotics and Intelligent Systems, as well as a forthcoming Master's in Data Science from the University of Oslo, I have honed my ability to tackle complex data challenges across various domains. "
        "<br>"
        "My experience includes developing predictive models for energy consumption, enhancing public services through AI, and applying advanced machine learning techniques in sports analytics.As a team lead, I have successfully guided cross-functional teams in creating innovative AI solutions, demonstrating my commitment to delivering high-quality, impactful results."
        "<br>"
        "Beyond my professional pursuits, I am deeply interested in fitness, particularly calisthenics and strength training💪, which help me stay disciplined and focused. I also have a keen interest in the financial markets, enjoying the challenges of trading and financial analysis 📊. A lifelong learner, I am constantly seeking to expand my knowledge, particularly in the rapidly evolving field of AI."
        "<br>"
        " Whether it's experimenting with new models or staying up-to-date with the latest technological advancements, I am driven by curiosity and a passion for continuous improvement."
        "<br>"
        "Thanks for visiting my portfolio! Feel free to connect with me on LinkedIn or mail 🚀"
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<div style='text-align: justify'>"
        "<br>"
        "<a href='https://www.linkedin.com/in/said-h-1956b0161/'><img src='https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png' width='40'></a>"
        "&nbsp;&nbsp;&nbsp;&nbsp;"
        "<a href='https://github.com/Shirdarec'><img src='https://upload.wikimedia.org/wikipedia/commons/c/c2/GitHub_Invertocat_Logo.svg' width='40'></a>"
        "&nbsp;&nbsp;&nbsp;&nbsp;"
        "<a href='mailto:saidhem@student.matnat.uio.no'><img src='https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png' width='40'></a>"
        "</div>",
        unsafe_allow_html=True,
    )
