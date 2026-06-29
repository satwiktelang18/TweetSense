import streamlit as st
from chatbot import predict_sentiment

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="TweetSense AI",
    page_icon="🐦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""

<style>

/* ---------- Hide Streamlit Menu ---------- */

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

/* ---------- Main ---------- */

.block-container{
padding-top:2rem;
padding-bottom:2rem;
padding-left:4rem;
padding-right:4rem;
}

.main{
background:#0E1117;
}

/* ---------- Title ---------- */

.title{
font-size:56px;
font-weight:800;
color:white;
margin-bottom:0px;
}

.subtitle{

font-size:22px;
font-weight:600;
color:#E5E7EB;

margin-top:-8px;
margin-bottom:5px;

}

.desc{

font-size:16px;
color:#B8C1CC;
margin-bottom:25px;

}

/* ---------- Cards ---------- */

.card{

background:#161B22;

padding:22px;

border-radius:18px;

border:1px solid #30363D;

box-shadow:0px 6px 18px rgba(0,0,0,0.35);

}

/* ---------- Text Area ---------- */

textarea{

background:#F8FAFC !important;
color:#000000 !important;
font-size:24px !important;
font-weight:500;
line-height:1.7 !important;
border-radius:15px !important;
caret-color:#3B82F6 !important;

}

textarea::placeholder{

font-size:18px;

color:#808080 !important;

}

textarea:focus{

border:2px solid #60A5FA !important;

box-shadow:0px 0px 10px rgba(96,165,250,0.65) !important;

}

/* ---------- Button ---------- */

.stButton>button{

width:100%;

height:56px;

font-size:20px;

font-weight:bold;

border-radius:14px;

background:#2563EB;

color:white;

border:none;

transition:0.3s;

}

.stButton>button:hover{

background:#3B82F6;

transform:translateY(-2px);

box-shadow:0px 0px 16px rgba(59,130,246,.6);

}

/* ---------- Headings ---------- */

.section{

font-size:30px;

font-weight:700;

margin-bottom:15px;

color:white;

}

.metricTitle{

font-size:18px;

font-weight:600;

color:#E5E7EB;

margin-top:8px;

}

/* ---------- Prediction ---------- */

.good{

padding:18px;

background:#16351F;

border-radius:12px;

border-left:6px solid #22C55E;

font-size:22px;

font-weight:bold;

color:#A7F3D0;

}

.bad{

padding:18px;

background:#3B1717;

border-radius:12px;

border-left:6px solid #EF4444;

font-size:22px;

font-weight:bold;

color:#FECACA;

}

/* ---------- Footer ---------- */

.footer{

margin-top:30px;

padding:18px;

background:#161B22;

border-radius:16px;

text-align:center;

color:#B8C1CC;

font-size:15px;

border:1px solid #30363D;

}

</style>

""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

st.markdown(
"""
<div class="title">
TweetSense AI
</div>

<div class="subtitle">
Twitter Sentiment Analysis using Sentiment140
</div>

<div class="desc">
Analyze any tweet using a Machine Learning model trained on the
Sentiment140 dataset with TF-IDF Vectorization and Logistic Regression.
</div>
""",
unsafe_allow_html=True
)

st.divider()

# ==========================================================
# LANDSCAPE LAYOUT
# ==========================================================

left, right = st.columns([1.2,1], gap="large")

# ==========================================================
# LEFT SIDE
# ==========================================================

with left:

    st.markdown(
    "<div class='section'>Enter Tweet</div>",
    unsafe_allow_html=True
    )

    tweet = st.text_area(

        "",

        height=260,

        placeholder="Enter Your Tweet Here...."

    )

    analyze = st.button(
        "🚀 Analyze Sentiment",
        use_container_width=True
    )

    st.markdown(
    "</div>",
    unsafe_allow_html=True
    )

# ==========================================================
# RIGHT SIDE
# ==========================================================

with right:

    prediction_placeholder = st.empty()

# ==========================================================
# RIGHT PANEL
# ==========================================================

if analyze:

    if tweet.strip() == "":

        with prediction_placeholder.container():

            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.warning("Please enter a tweet first.")
            st.markdown("</div>", unsafe_allow_html=True)

    else:

        sentiment, confidence, probabilities = predict_sentiment(tweet)

        if sentiment == "positive":

            explanation = """
This tweet contains words that indicate happiness, appreciation,
satisfaction or excitement. The model believes the overall tone
is positive.
"""

        else:

            explanation = """
This tweet contains words expressing frustration, disappointment,
anger or dissatisfaction. The model predicts an overall
negative sentiment.
"""

        with prediction_placeholder.container():

            st.markdown(
                "<div class='section'>Prediction</div>",
                unsafe_allow_html=True
            )

            if sentiment == "positive":

                st.markdown(
                    """
<div class='good'>
🟢 Positive Tweet 
</div>
""",
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    """
<div class='bad'>
🔴 Negative Tweet
</div>
""",
                    unsafe_allow_html=True
                )

            st.write("")

            # ==========================================
            # Confidence
            # ==========================================

            st.markdown(
                "<div class='metricTitle'>Confidence</div>",
                unsafe_allow_html=True
            )

            positive = probabilities["positive"] * 100
            negative = probabilities["negative"] * 100

            st.write("Positive")

            st.progress(positive / 100)

            st.markdown(
                f"""
<div style="text-align:right;
font-size:26px;
font-weight:700;
color:#22C55E;
margin-bottom:20px;">
{positive:.2f}%
</div>
""",
                unsafe_allow_html=True
            )

            st.write("Negative")

            st.progress(negative / 100)

            st.markdown(
                f"""
<div style="text-align:right;
font-size:26px;
font-weight:700;
color:#EF4444;">
{negative:.2f}%
</div>
""",
                unsafe_allow_html=True
            )

            st.divider()

            # ==========================================
            # Explanation
            # ==========================================

            st.markdown(
                "<div class='metricTitle'>AI Explanation</div>",
                unsafe_allow_html=True
            )

            st.info(explanation)

            st.markdown("</div>", unsafe_allow_html=True)
else:

    with prediction_placeholder.container():

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.markdown(
            "<div class='section'>📊 Prediction</div>",
            unsafe_allow_html=True
        )

        st.markdown(
"""
<div style="text-align:center;
padding-top:35px;
padding-bottom:35px;">

<h2 style="color:#B8C1CC;">
Waiting for your tweet...
</h2>

<p style="font-size:18px;color:#9CA3AF;">
Enter a tweet on the left and click
<b>Analyze Sentiment</b>.
</p>

</div>
""",
unsafe_allow_html=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

# ==========================================================
# SPACING
# ==========================================================

st.write("")
st.write("")
st.divider()

# ==========================================================
# MODEL INFORMATION
# ==========================================================

st.markdown(
"""
<div class='footer'>

Built with ❤️ by Satwik!

TF-IDF Vectorizer + Logistic Regression trained on the
Sentiment140 Twitter Dataset.

</div>
""",
unsafe_allow_html=True
)