
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

print("\n ANALYSIS COMPLETE ")
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

#Keyword Overlap
from sklearn.feature_extraction.text import CountVectorizer

print("\n KEYWORD OVERLAP ")

overlap_metrics = []

for comp, docs in data.items():
    if not docs["ai"] or not docs["official"]: continue
    
    ai_low = docs["ai"].lower()
    off_low = docs["official"].lower()
    
    cv = CountVectorizer(stop_words='english', max_features=50)
    try:
        cv.fit([docs["ai"], docs["official"]])
        words = cv.get_feature_names_out()
        
        shared = [w for w in words if w in ai_low and w in off_low][:5]
        overlap_str = ", ".join(shared)
    except Exception:
        overlap_str = "None"
        
    overlap_metrics.append({
        "Company": comp.upper(),
        "Top_Overlapping_Keywords": overlap_str
    })

df_overlap = pd.DataFrame(overlap_metrics)
df_overlap.to_csv(BASE_DIR / "results" / "classical_keyword_overlap.csv", index=False)

print(df_overlap.to_string(index=False))

#ESG Topic Coverage
print("\n STRUCTURAL ESG TOPIC COVERAGE ")

coverage_density_metrics = []

esg_themes = {
    "Environmental": ["carbon", "emission", "climate", "energy", "environmental", "sustainability"],
    "Social": ["employee", "diversity", "safety", "social", "human", "community", "labor"],
    "Governance": ["board", "governance", "compliance", "ethics", "audit", "shareholder", "policy"]
}

for comp, docs in data.items():
    if not docs["ai"] or not docs["official"]: continue
    
    ai_sents = nltk.sent_tokenize(docs["ai"])
    off_sents = nltk.sent_tokenize(docs["official"])
    
    ai_total = len(ai_sents)
    off_total = len(off_sents)
    
    def calc_density(sentences, keywords, total_count):
        if total_count == 0: return 0.0
        matching_sents = sum(1 for s in sentences if any(k in s.lower() for k in keywords))
        return round((matching_sents / total_count) * 100, 2)

    coverage_density_metrics.append({
        "Company": comp.upper(),
        "AI_Env_Coverage_%": calc_density(ai_sents, esg_themes["Environmental"], ai_total),
        "Off_Env_Coverage_%": calc_density(off_sents, esg_themes["Environmental"], off_total),
        "AI_Soc_Coverage_%": calc_density(ai_sents, esg_themes["Social"], ai_total),
        "Off_Soc_Coverage_%": calc_density(off_sents, esg_themes["Social"], off_total),
        "AI_Gov_Coverage_%": calc_density(ai_sents, esg_themes["Governance"], ai_total),
        "Off_Gov_Coverage_%": calc_density(off_sents, esg_themes["Governance"], off_total),
    })

df_density = pd.DataFrame(coverage_density_metrics)
df_density.to_csv(BASE_DIR / "results" / "classical_esg_structural_coverage.csv", index=False)

print(df_density.to_string(index=False))

#Topic Specific Sentiment Analysis

print("\n TOPIC-SPECIFIC SENTIMENT ANALYSIS ")

topic_sentiment_metrics = []

for comp, docs in data.items():
    if not docs["ai"] or not docs["official"]: continue
    
    ai_sents = nltk.sent_tokenize(docs["ai"])
    off_sents = nltk.sent_tokenize(docs["official"])
    
    def get_theme_sentiment(sentences, keywords):
        matching_text = " ".join([s for s in sentences if any(k in s.lower() for k in keywords)])
        if not matching_text.strip(): return 0.0
        return round(TextBlob(matching_text).sentiment.polarity, 4)
        
    topic_sentiment_metrics.append({
        "Company": comp.upper(),
        "AI_Env_Sent": get_theme_sentiment(ai_sents, esg_themes["Environmental"]),
        "Off_Env_Sent": get_theme_sentiment(off_sents, esg_themes["Environmental"]),
        "AI_Soc_Sent": get_theme_sentiment(ai_sents, esg_themes["Social"]),
        "Off_Soc_Sent": get_theme_sentiment(off_sents, esg_themes["Social"]),
        "AI_Gov_Sent": get_theme_sentiment(ai_sents, esg_themes["Governance"]),
        "Off_Gov_Sent": get_theme_sentiment(off_sents, esg_themes["Governance"])
    })

df_topic_sent = pd.DataFrame(topic_sentiment_metrics)
df_topic_sent.to_csv(BASE_DIR / "results" / "classical_topic_sentiment.csv", index=False)

print(df_topic_sent.to_string(index=False))