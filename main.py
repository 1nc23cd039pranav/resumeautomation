import pdfplumber
import google.generativeai as genai

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        for page in pdf.pages:
            full_text += page.extract_text()
    return full_text

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel('gemini-pro')

def generate_tailored_resume(jd_text, resume_text):
    prompt = f"Analyze this JD: {jd_text} and my resume: {resume_text}... (insert strategy above)"
    response = model.generate_content(prompt)
    return response.text