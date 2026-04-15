RESUME AUTOMATION
a platform for students and job hunters

Its a platform developed to analyze your resume and search jobs according to your resume and also give you a feedback that what are the skills reuired or you have to change in your resume to land a job.

The Tech Stack
To keep this robust and modern, we will use:

Language: Python
LLM: Google Gemini API 
Parsing: PyPDF2 or pdfplumber (to read your resume)
Document Generation: python-docx (to create the new resume)
Orchestration: LangChain

Step 1: Document Parsing
You need to convert your static PDF resume into a structured format (JSON) that an AI can manipulate.
