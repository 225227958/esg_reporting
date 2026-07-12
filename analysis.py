import os
from pathlib import Path
from pypdf import PdfReader

# Dynamically targets the folder where this script lives
BASE_DIR = Path(__file__).resolve().parent
Generated_Dir = BASE_DIR / "reports" / "generated"
Actual_Dir = BASE_DIR / "reports" / "actual"

companies = ["lvmh", "hugoboss", "exxonmobil", "rwe"]
corpus = {}

def extract_text_from_pdf(pdf_path):
    # Ensure compatibility with os.path and pypdf
    pdf_path_str = str(pdf_path)
    if not os.path.exists(pdf_path_str):
        print(f"Warning: File not found at {pdf_path_str}")
        return ""
    
    try:
        reader = PdfReader(pdf_path_str)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text  
        
    except Exception as e:
        print(f"Error reading {pdf_path_str}: {e}") 
        return ""  

print("STARTING DOCUMENT LOADING PROCESS")
for comp in companies:
    ai_file = Generated_Dir / f"{comp}_generated.pdf"
    off_file = Actual_Dir / f"{comp}_actual.pdf"

    corpus[comp] = {
        "ai": extract_text_from_pdf(ai_file),
        "official": extract_text_from_pdf(off_file)
    }
    print(f"[{comp.upper()}] Loaded successfully.")
    print(f" --> AI text length: {len(corpus[comp]['ai'])} characters")
    print(f" --> Official text length: {len(corpus[comp]['official'])} characters")