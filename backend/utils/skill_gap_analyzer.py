from backend.utils.job_roles import JOB_ROLES

def analyze_skill_gap(user_skills, target_role):

    required_skills = JOB_ROLES.get(target_role, [])

    matched_skills = []
    missing_skills = []

    for skill in required_skills:

        if skill.lower() in [s.lower() for s in user_skills]:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    match_percentage = (
        len(matched_skills) / len(required_skills)
    ) * 100 if required_skills else 0

    return {
        "target_role": target_role,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_percentage": round(match_percentage, 2)
    }