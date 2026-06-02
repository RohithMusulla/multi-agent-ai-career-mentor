from crewai import Task, Crew

from backend.agents.career_agents import (
    resume_agent,
    skill_gap_agent,
    roadmap_agent,
    interview_agent
)


def run_career_crew(
    resume_text,
    target_role
):

    # Resume Analysis Task
    resume_task = Task(

        description=f"""
        Analyze this resume:

        {resume_text}

        Identify:
        - strengths
        - weaknesses
        - technical skills
        """,

        expected_output="""
        Detailed resume analysis
        including strengths,
        weaknesses, and skills.
        """,

        agent=resume_agent
    )

    # Skill Gap Task
    skill_gap_task = Task(

        description=f"""
        Identify missing skills
        for becoming a
        {target_role}.
        """,

        expected_output="""
        List of missing skills
        required for the role.
        """,

        agent=skill_gap_agent
    )

    # Roadmap Task
    roadmap_task = Task(

        description=f"""
        Create a detailed
        learning roadmap
        for becoming a
        {target_role}.
        """,

        expected_output="""
        Step-by-step learning roadmap.
        """,

        agent=roadmap_agent
    )

    # Interview Task
    interview_task = Task(

        description=f"""
        Generate interview
        preparation guidance
        for a {target_role}.
        """,

        expected_output="""
        Interview preparation tips
        and likely questions.
        """,

        agent=interview_agent
    )

    crew = Crew(

        agents=[
            resume_agent,
            skill_gap_agent,
            roadmap_agent,
            interview_agent
        ],

        tasks=[
            resume_task,
            skill_gap_task,
            roadmap_task,
            interview_task
        ],

        verbose=True
    )

    result = crew.kickoff()

    return result