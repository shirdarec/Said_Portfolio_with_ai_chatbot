from streamlit_pills import pills
import json
# Function to load a JSON file

with open(r'data/technical_skills.json') as file:
    description = json.load(file)

right_column, left_column = st.columns([2, 1])
with right_column:
    st.title("Techincal Skills")
    skills = [
        "Microservices",
        "Large Language Model (LLM)",
        "Small Language Model (SLM)",
        "Fine Tuning",
        "Vector Database",
        "Prompt Engineering",
        "Docker",
        "Kubernetes",
        "MongoDB",
        "API",
        "Data Mining",
        "Data Analytics",
        "JSON",
        "Python/R",
        "Data Visualization",
        "Jupyter Notebook",
        "Excel",
        "Machine Learning Algorithms",
        "Automation",
        "ETL Pipeline",
        "Virtual Machine",
        "Architecture",
        "Azure",
        "Bash",
        "Cloud",
        "Network and System Scanning Tools",
        "Code",
        "Compliance",
        "GitLab",
        "Linux",
        "Python",
        "Reporting",
        "Strategy",
        "Technical Writing",
    ]
    selected = pills("Select a category", skills)

"""with left_column:
    st.title("Description")
    for skill in description["skills"]:
        if selected==skill["name"]:
            st.markdown(skill["description"])"""