
#Classical text analysis and similarity metrics
import os
import pandas as pd
from pathlib import Path
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = Path(__file__).resolve().parent
companies = ["lvmh", "hugoboss", "exxonmobil", "rwe"]

def extract_text(path):
    """Extracts raw text from a PDF cleanly."""
    if not path.exists(): return ""
    try:
        return "\n".join([p.extract_text() for p in PdfReader(str(path)).pages if p.extract_text()])
    except Exception:
        return ""

data = {
    comp: {
        "ai": extract_text(BASE_DIR / "reports" / "generated" / f"{comp}_generated.pdf"),
        "official": extract_text(BASE_DIR / "reports" / "actual" / f"{comp}_actual.pdf")
    } for comp in companies
}

metrics = []
for comp, docs in data.items():
    if not docs["ai"] or not docs["official"]: continue
    
    tfidf = TfidfVectorizer(stop_words='english').fit_transform([docs["ai"], docs["official"]])
    similarity = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    
    ai_words, off_words = len(docs["ai"].split()), len(docs["official"].split())
    
    metrics.append({
        "Company": comp.upper(),
        "AI_Word_Count": ai_words,
        "Official_Word_Count": off_words,
        "Length_Ratio": round(ai_words / off_words, 4),
        "Cosine_Similarity": round(similarity, 4)
    })

df = pd.DataFrame(metrics)
os.makedirs(BASE_DIR / "results", exist_ok=True)
df.to_csv(BASE_DIR / "results" / "classical_analysis_summary.csv", index=False)

print("\n--- ANALYSIS COMPLETE ---")
print(df.to_string(index=False))