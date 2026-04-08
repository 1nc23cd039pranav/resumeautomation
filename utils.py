def missing_skills(jd_skills, resume_text):
    resume_lower = resume_text.lower()
    missing = []

    for skill in jd_skills:
        if skill.lower() not in resume_lower:
            missing.append(skill)

    return missing