import pickle
import re

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# ==========================================
# Load Model
# ==========================================

model = pickle.load(open("model/model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

stemmer = PorterStemmer()
nltk.download("stopwords", quiet=True)
stop_words = set(stopwords.words("english"))

# ==========================================
# Clean Text
# ==========================================

def clean_text(text):

    text = text.lower()

    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#", "", text)
    text = re.sub(r"[^a-zA-Z]", " ", text)

    words = text.split()

    words = [
        stemmer.stem(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)

# ==========================================
# Predict Sentiment
# ==========================================

def predict_sentiment(text):

    cleaned = clean_text(text)

    vector = vectorizer.transform([cleaned])

    sentiment = model.predict(vector)[0]

    proba = model.predict_proba(vector)[0]

    probability_dict = dict(zip(model.classes_, proba))

    positive_prob = probability_dict["positive"]
    negative_prob = probability_dict["negative"]

    confidence = max(positive_prob, negative_prob)

    return (
        sentiment,
        confidence,
        {
            "positive": positive_prob,
            "negative": negative_prob
        }
    )
