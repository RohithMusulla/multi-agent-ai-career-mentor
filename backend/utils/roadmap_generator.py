from backend.utils.openai_client import client

def generate_learning_roadmap(
    target_role,
    missing_skills
):

    prompt = f"""
    You are an AI Career Mentor.

    The user wants to become a {target_role}.

    Missing Skills:
    {missing_skills}

    Create:
    1. 3-month roadmap
    2. Weekly learning plan
    3. Recommended projects
    4. Interview preparation tips
    5. Certification recommendations

    Keep it beginner-friendly.
    """

    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content