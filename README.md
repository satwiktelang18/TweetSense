<div align="center">

# TweetSense AI

### Twitter Sentiment Analysis using Machine Learning

Analyze tweets in real-time using a Machine Learning model trained on the **Sentiment140** dataset with **TF-IDF Vectorization** and **Logistic Regression**.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-purple?style=for-the-badge&logo=pandas)
![NLTK](https://img.shields.io/badge/NLTK-NLP-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

</div>

---

# Overview

TweetSense AI is a Machine Learning web application that predicts whether a tweet expresses **Positive** or **Negative** sentiment.

The application performs automatic text preprocessing, transforms tweets into numerical vectors using **TF-IDF**, and classifies them using a trained **Logistic Regression** model.

The web interface is built using **Streamlit** and provides real-time predictions with confidence scores.

---

# Features 

- ✅ Real-time tweet sentiment prediction
- ✅ Clean and responsive Streamlit UI
- ✅ TF-IDF Vectorization
- ✅ Logistic Regression classifier
- ✅ Text preprocessing using NLTK
- ✅ Confidence score visualization
- ✅ AI explanation for every prediction
- ✅ CSV batch prediction for tweet export files
- ✅ Lightweight and fast inference

---

# Application Preview

<img width="1470" height="799" alt="Screenshot 2026-06-29 at 8 16 01 PM" src="https://github.com/user-attachments/assets/d2ee4bc4-e08a-4e29-8af6-5d48eb6120f6" />



# Machine Learning Pipeline

```
Tweet
   │
   ▼
Text Cleaning
   │
   ▼
Tokenization
   │
   ▼
Stopword Removal
   │
   ▼
Porter Stemming
   │
   ▼
TF-IDF Vectorizer
   │
   ▼
Logistic Regression
   │
   ▼
Positive / Negative Prediction
```

---

# Technologies Used

- Python
- Streamlit
- Scikit-Learn
- Pandas
- NLTK
- Pickle
- TF-IDF Vectorizer
- Logistic Regression

---

# Project Structure

```
TweetSense/
│
├── model/
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── app.py
├── chatbot.py
├── train.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Dataset

This project is trained on the **Sentiment140 Dataset**.

Dataset Characteristics:

- 1.6 Million Tweets
- Binary Sentiment Classification
- Positive and Negative Sentiments
- Twitter Data

> **Note:** The dataset is intentionally excluded from this repository because it exceeds GitHub's file size limit.

---

# Installation

Clone the repository

```bash
git clone https://github.com/satwiktelang18/TweetSense.git
```

Move into the project

```bash
cd TweetSense
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# Usage

1. Launch the Streamlit application.
2. Enter any tweet.
3. Click **Analyze Sentiment**.
4. View:
   - Predicted Sentiment
   - Confidence Scores
   - AI Explanation
5. Or upload a CSV with `tweet`, `text`, `full_text`, `content`, `body`, or
   `message` columns to score a batch of reviewed X/Twitter exports from
   TweetClaw, OpenClaw plugins, or similar tools.

---

# Model Information

| Model | Logistic Regression |
|--------|---------------------|
| Vectorizer | TF-IDF |
| NLP | NLTK |
| Classification | Binary |
| Dataset | Sentiment140 |

---

# 💡 Future Improvements

- Support Neutral Sentiment
- Emotion Detection
- Transformer-based Models (BERT)
- Twitter API Integration
- Aspect-based Sentiment Analysis
- Model Comparison Dashboard

---

# 👨‍💻 Author

**Satwik Telang**
