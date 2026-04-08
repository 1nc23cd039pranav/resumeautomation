import streamlit as st
from jd_parser import extract_jd_requirements
from ats_matcher import calculate_ats_score
from utils import missing_skills

st.set_page_config(page_title="ATS Resume Automation", layout="wide")

st.title("AI ATS Resume Analyzer")
st.write("Paste Job Description and Resume text below")

jd_text = st.text_area("Paste Job Description", height=250)
resume_text = st.text_area("Paste Resume Text", height=250)

if st.button("Analyze Resume"):
    if jd_text and resume_text:
        jd_data = extract_jd_requirements(jd_text)
        score = calculate_ats_score(jd_text, resume_text)
        missing = missing_skills(jd_data["skills"], resume_text)

        st.subheader("ATS Analysis Result")
        st.write(f"ATS Score: {score}%")
        st.write("Matched Skills:", jd_data["skills"])
        st.write("Missing Skills:", missing)
    else:
        st.warning("Please paste both JD and Resume text")