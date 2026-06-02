from fastapi import APIRouter

from backend.rag.rag_pipeline import ask_career_question

router = APIRouter()


@router.get("/career-chat")

def career_chat(question: str):

    answer = ask_career_question(question)

    return {
        "question": question,
        "answer": answer
    }