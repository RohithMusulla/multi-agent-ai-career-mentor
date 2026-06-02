SKILLS_DB = [
    "Python",
    "Java",
    "C++",
    "SQL",
    "Machine Learning",
    "Deep Learning",
    "TensorFlow",
    "PyTorch",
    "FastAPI",
    "React",
    "Node.js",
    "MongoDB",
    "PostgreSQL",
    "Docker",
    "Kubernetes",
    "AWS",
    "Data Analysis",
    "NLP"
]

def extract_skills(resume_text):
    found_skills = []

    for skill in SKILLS_DB:
        if skill.lower() in resume_text.lower():
            found_skills.append(skill)

    return list(set(found_skills))