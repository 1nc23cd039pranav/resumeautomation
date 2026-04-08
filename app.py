from jd_parser import extract_jd_requirements
from resume_parser import read_resume_docx
from ats_matcher import calculate_ats_score
from resume_generator import generate_tailored_resume
from utils import missing_skills

JD_FILE = "data/sample_jd.txt"
RESUME_FILE = "data/master_resume.docx"
OUTPUT_FILE = "output/tailored_resume.docx"

with open(JD_FILE, "r", encoding="utf-8") as f:
    jd_text = f.read()

resume_text = read_resume_docx(RESUME_FILE)

jd_data = extract_jd_requirements(jd_text)
score = calculate_ats_score(jd_text, resume_text)
missing = missing_skills(jd_data["skills"], resume_text)

generate_tailored_resume(
    RESUME_FILE,
    OUTPUT_FILE,
    jd_data["skills"],
    score
)

print("ATS Score:", score)
print("Missing Skills:", missing)
print("Tailored resume saved successfully")