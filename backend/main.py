from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI

from backend.routes.resume_routes import router as resume_router
from backend.routes.chat_routes import router as chat_router
from backend.routes.agent_routes import router as agent_router

app = FastAPI()

app.include_router(resume_router)
app.include_router(chat_router)
app.include_router(agent_router)


@app.get("/")
def home():

    return {
        "message": "Career Mentor AI Running"
    }