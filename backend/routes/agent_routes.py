from fastapi import APIRouter

from backend.agents.career_crew import run_career_crew

router = APIRouter()


@router.post("/multi-agent-analysis")

def multi_agent_analysis():

    sample_resume = """
    Python developer with SQL,
    FastAPI, machine learning,
    and AI skills.
    """

    result = run_career_crew(
        sample_resume,
        "Data Scientist"
    )

    return {
        "multi_agent_result": str(result)
    }