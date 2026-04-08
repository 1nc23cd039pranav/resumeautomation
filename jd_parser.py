import re
import spacy

nlp = spacy.load("en_core_web_sm")

COMMON_SKILLS = [
    "python", "sql", "tensorflow", "pandas", "machine learning",
    "deep learning", "nlp", "power bi", "excel", "aws",
    "docker", "git", "scikit-learn", "streamlit"
]


def extract_jd_requirements(job_text):
    text = job_text.lower()
    found_skills = []

    for skill in COMMON_SKILLS:
        if skill in text:
            found_skills.append(skill)

    doc = nlp(job_text)
    keywords = [token.text.lower() for token in doc if token.is_alpha and not token.is_stop]

    return {
        "skills": list(set(found_skills)),
        "keywords": list(set(keywords))
    }