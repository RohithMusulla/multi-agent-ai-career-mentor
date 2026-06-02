from backend.utils.openai_client import client


def ask_career_question(question):

    prompt = f"""
    You are an AI Career Mentor.

    Answer the following career question
    in a beginner-friendly and professional way.

    Question:
    {question}
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