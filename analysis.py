
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

#Extended Classical Text Analysis

import nltk
from textblob import TextBlob
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

print("\n RUNNING ADD_ON METRICS (SENTENCES, VOCABULARY, SENTIMENT)")

extended_metrics = []
esg_terms = ["scope 3", "materiality", "tcfd"]

for comp, docs in data.items():
    if not docs["ai"] or not docs["official"]: continue
    
    ai_sents = nltk.sent_tokenize(docs["ai"])
    off_sents = nltk.sent_tokenize(docs["official"])
    
    ai_sent_count = len(ai_sents)
    off_sent_count = len(off_sents)
    
    ai_words_count = len(docs["ai"].split())
    off_words_count = len(docs["official"].split())
    ai_avg_sent_len = round(ai_words_count / ai_sent_count, 2) if ai_sent_count > 0 else 0
    off_avg_sent_len = round(off_words_count / off_sent_count, 2) if off_sent_count > 0 else 0

    ai_lower = docs["ai"].lower()
    off_lower = docs["official"].lower()
    
    ai_vocab_counts = {term: ai_lower.count(term) for term in esg_terms}
    off_vocab_counts = {term: off_lower.count(term) for term in esg_terms}

    ai_sentiment = round(TextBlob(docs["ai"]).sentiment.polarity, 4)
    off_sentiment = round(TextBlob(docs["official"]).sentiment.polarity, 4)

    extended_metrics.append({
        "Company": comp.upper(),
        "AI_Sentences": ai_sent_count,
        "Off_Sentences": off_sent_count,
        "AI_Avg_Sent_Len": ai_avg_sent_len,
        "Off_Avg_Sent_Len": off_avg_sent_len,
        "AI_Scope3": ai_vocab_counts["scope 3"],
        "Off_Scope3": off_vocab_counts["scope 3"],
        "AI_Materiality": ai_vocab_counts["materiality"],
        "Off_Materiality": off_vocab_counts["materiality"],
        "AI_TCFD": ai_vocab_counts["tcfd"],
        "Off_TCFD": off_vocab_counts["tcfd"],
        "AI_Sentiment": ai_sentiment,
        "Off_Sentiment": off_sentiment
    })
df_extended = pd.DataFrame(extended_metrics)
df_extended.to_csv(BASE_DIR / "results" / "classical_extended_analysis.csv", index=False)

print("\n ADDITIONAL METRICS TABLE ")
print(df_extended.to_string(index=False))

#Jaccard Similarity

print("\n JACCARD SIMILARITY ")

jaccard_metrics = []

for comp, docs in data.items():
    if not docs["ai"] or not docs["official"]: continue
    
    ai_set = set(docs["ai"].lower().split())
    off_set = set(docs["official"].lower().split())
    
    intersection = len(ai_set.intersection(off_set))
    union = len(ai_set.union(off_set))
    jaccard_sim = round(intersection / union, 4) if union > 0 else 0
    
    jaccard_metrics.append({
        "Company": comp.upper(),
        "Jaccard_Similarity": jaccard_sim
    })

df_jaccard = pd.DataFrame(jaccard_metrics)
df_jaccard.to_csv(BASE_DIR / "results" / "classical_jaccard.csv", index=False)

print(df_jaccard.to_string(index=False))
