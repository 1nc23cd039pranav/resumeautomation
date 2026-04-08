The Tech Stack
To keep this robust and modern, we will use:

Language: Python
LLM: Google Gemini API 
Parsing: PyPDF2 or pdfplumber (to read your resume)
Document Generation: python-docx (to create the new resume)
Orchestration: LangChain

Step 1: Document Parsing
You need to convert your static PDF resume into a structured format (JSON) that an AI can manipulate.