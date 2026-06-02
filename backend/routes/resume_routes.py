from fastapi import APIRouter, UploadFile, File
import shutil
import os

from backend.utils.pdf_extractor import extract_text_from_pdf
from backend.utils.skill_extractor import extract_skills
from backend.utils.skill_gap_analyzer import analyze_skill_gap
from backend.utils.roadmap_generator import generate_learning_roadmap

router = APIRouter()

UPLOAD_FOLDER = "uploads"


@router.post("/upload-resume")
async def upload_resume(
    file: UploadFile = File(...),
    target_role: str = "Data Scientist"
):

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    file_path = f"{UPLOAD_FOLDER}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract Resume Text
    resume_text = extract_text_from_pdf(file_path)

    # Extract Skills
    skills = extract_skills(resume_text)

    # Analyze Skill Gap
    skill_gap = analyze_skill_gap(skills, target_role)

    roadmap = generate_learning_roadmap(
    target_role,
    skill_gap["missing_skills"]
    )

    return {
        "filename": file.filename,
        "detected_skills": skills,
        "skill_gap_analysis": skill_gap,
        "resume_preview": resume_text[:1000]
    }