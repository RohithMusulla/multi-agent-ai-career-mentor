from dotenv import load_dotenv
load_dotenv()

from crewai import Agent
from langchain_openai import ChatOpenAI


# Create shared LLM object
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7
)


# Resume Analyzer Agent
resume_agent = Agent(
    role="Resume Analyzer",

    goal="""
    Analyze resumes and identify
    strengths, weaknesses,
    and technical skills.
    """,

    backstory="""
    You are an expert resume reviewer
    with deep knowledge of
    AI, software engineering,
    and recruitment.
    """,

    verbose=True,

    llm=llm
)


# Skill Gap Agent
skill_gap_agent = Agent(
    role="Skill Gap Expert",

    goal="""
    Identify missing skills
    required for target job roles.
    """,

    backstory="""
    You specialize in analyzing
    industry skill requirements
    and career growth paths.
    """,

    verbose=True,

    llm=llm
)


# Roadmap Agent
roadmap_agent = Agent(
    role="Learning Roadmap Generator",

    goal="""
    Create structured learning plans
    for career growth.
    """,

    backstory="""
    You are an expert mentor
    helping students become
    AI engineers and developers.
    """,

    verbose=True,

    llm=llm
)


# Interview Coach Agent
interview_agent = Agent(
    role="Interview Coach",

    goal="""
    Prepare users for interviews
    with practical guidance.
    """,

    backstory="""
    You are a senior technical
    interviewer with expertise
    in AI and software roles.
    """,

    verbose=True,

    llm=llm
)
