import re
import pickle
import nltk
import pandas as pd

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# ==========================================
# Download NLTK Stopwords
# ==========================================

nltk.download("stopwords")

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv(
    "dataset/training.1600000.processed.noemoticon.csv",
    encoding="latin-1",
    header=None
)

df.columns = [
    "target",
    "id",
    "date",
    "flag",
    "user",
    "text"
]

# ==========================================
# Convert labels
# ==========================================

df["target"] = df["target"].replace({
    0: "negative",
    4: "positive"
})

df = df[df["target"].isin(["negative", "positive"])]

print("\nLabels after filtering:")
print(df["target"].value_counts())

# ==========================================
# Random sample
# ==========================================

df = df.sample(
    n=100000,
    random_state=42
)

df = df[["text", "target"]]

# ==========================================
# Text Cleaning
# ==========================================

stemmer = PorterStemmer()
stop_words = set(stopwords.words("english"))

def clean_text(text):

    text = str(text).lower()

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

print("Cleaning Tweets...")

df["text"] = df["text"].apply(clean_text)

# ==========================================
# Features
# ==========================================

X = df["text"]
y = df["target"]

# ==========================================
# TF-IDF
# ==========================================

vectorizer = TfidfVectorizer(
    max_features=5000
)

X = vectorizer.fit_transform(X)

# ==========================================
# Train Test Split
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ==========================================
# Logistic Regression
# ==========================================

model = LogisticRegression(
    max_iter=1000,
    random_state=42
)

model.fit(X_train, y_train)

# ==========================================
# Evaluation
# ==========================================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print(f"\nAccuracy : {accuracy*100:.2f}%\n")

print(classification_report(y_test, y_pred))

print("\nClasses learned by model:")
print(model.classes_)

# ==========================================
# Save
# ==========================================

pickle.dump(
    model,
    open("model/model.pkl", "wb")
)

pickle.dump(
    vectorizer,
    open("model/vectorizer.pkl", "wb")
)

print("\nModel Saved Successfully!")