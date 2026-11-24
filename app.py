
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import matplotlib.pyplot as plt
import textwrap

from pathlib import Path
from sklearn.metrics import ConfusionMatrixDisplay

# ==========================================
# PHISHSENSE - EMAIL SECURITY DASHBOARD
# ==========================================

BASE_DIR = Path(__file__).parent
MODEL_DIR = BASE_DIR / "models"

st.set_page_config(
    page_title="PhishSense",
    page_icon="🛡️",
    layout="wide"
)

# ==========================================
# CUSTOM STYLING
# ==========================================

st.markdown(
    textwrap.dedent("""
    <style>
    .stApp {
        background-color: #0B1424;
        color: #EAF2FF;
    }

    [data-testid="stSidebar"] {
        background-color: #101D30;
    }

    .block-container {
        padding-top: 2rem;
    }

    h1, h2, h3 {
        color: #EAF2FF !important;
    }

    .hero {
        background: linear-gradient(120deg, #142B48, #164A70);
        padding: 30px;
        border-radius: 16px;
        border: 1px solid #28618A;
        margin-bottom: 25px;
    }

    .hero h1 {
        color: white !important;
        font-size: 38px;
        margin-bottom: 8px;
    }

    .hero p {
        color: #C3D9EF;
    }

    .metric-card {
        background: linear-gradient(135deg, #142A43, #193B5C);
        padding: 22px;
        border-radius: 14px;
        border: 1px solid #284D70;
        min-height: 110px;
    }

    .metric-label {
        color: #A9C2DC;
        font-size: 14px;
    }

    .metric-value {
        color: white;
        font-size: 28px;
        font-weight: bold;
    }

    div.stButton > button {
        background-color: #1677C8;
        color: white;
        border-radius: 9px;
        border: none;
        font-weight: bold;
    }

    div.stButton > button:hover {
        background-color: #2496EA;
        color: white;
    }
    </style>
    """),
    unsafe_allow_html=True
)

# ==========================================
# LOAD TRAINED MODELS
# ==========================================

@st.cache_resource
def load_models():

    vectorizer = joblib.load(
        MODEL_DIR / "tfidf_vectorizer.joblib"
    )

    models = {
        "Random Forest": joblib.load(
            MODEL_DIR / "random_forest.joblib"
        ),

        "Logistic Regression": joblib.load(
            MODEL_DIR / "logistic_regression.joblib"
        ),

        "Naive Bayes": joblib.load(
            MODEL_DIR / "naive_bayes.joblib"
        ),

        "MLP Classifier": joblib.load(
            MODEL_DIR / "mlp.joblib"
        )
    }

    return vectorizer, models


try:
    vectorizer, models = load_models()
    models_loaded = True
    model_error = None

except Exception as e:
    vectorizer = None
    models = {}
    models_loaded = False
    model_error = str(e)


# ==========================================
# EXPERIMENTAL RESULTS
# ==========================================

results = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Random Forest",
        "Naive Bayes",
        "MLP Classifier"
    ],

    "Accuracy": [
        98.3816,
        98.7150,
        95.9995,
        98.4301
    ]
})

confusion_matrices = {

    "Logistic Regression": [
        [7772, 147],
        [120, 8459]
    ],

    "Random Forest": [
        [7810, 109],
        [103, 8476]
    ],

    "Naive Bayes": [
        [7806, 113],
        [547, 8032]
    ],

    "MLP Classifier": [
        [7810, 109],
        [150, 8429]
    ]

}


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.markdown("# 🛡️ PhishSense")
st.sidebar.caption("AI-POWERED EMAIL SECURITY")
st.sidebar.divider()

page = st.sidebar.radio(
    "NAVIGATION",
    [
        "Overview",
        "Email Scanner",
        "Model Analytics",
        "About Project"
    ]
)

st.sidebar.divider()

if models_loaded:
    st.sidebar.success("All 4 models loaded")
else:
    st.sidebar.error("Model loading failed")
    st.sidebar.caption(model_error)

st.sidebar.caption(
    "Built using NLP & Machine Learning"
)


# ==========================================
# HEADER
# ==========================================

st.markdown(
    textwrap.dedent("""
    <div class="hero">
        <h1>🛡️ PhishSense</h1>
        <p>Intelligent Phishing Email Detection System</p>
        <p>Powered by Natural Language Processing and Machine Learning</p>
    </div>
    """),
    unsafe_allow_html=True
)


# ==========================================
# PAGE 1: OVERVIEW
# ==========================================

if page == "Overview":

    st.subheader("System Overview")

    metrics = [
        ("Total Emails", "82,486"),
        ("Best Test Accuracy", "98.71%"),
        ("ML Classifiers", "4"),
        ("TF-IDF Features", "10,000")
    ]

    cols = st.columns(4)

    for col, (label, value) in zip(cols, metrics):

        col.markdown(
            textwrap.dedent(f"""
            <div class="metric-card">
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
            </div>
            """),
            unsafe_allow_html=True
        )

    st.write("")

    left, right = st.columns(2)

    with left:

        st.subheader("Model Accuracy Comparison")

        fig = px.bar(
            results,
            x="Model",
            y="Accuracy",
            color="Model",
            text="Accuracy",
            range_y=[90, 101],
            template="plotly_dark"
        )

        fig.update_traces(
            texttemplate="%{text:.2f}%",
            textposition="outside"
        )

        fig.update_layout(
            showlegend=False,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )

        st.plotly_chart(fig, use_container_width=True)

    with right:

        st.subheader("Dataset Distribution")

        dataset = pd.DataFrame({
            "Category": ["Phishing", "Legitimate"],
            "Count": [42891, 39595]
        })

        fig = px.pie(
            dataset,
            names="Category",
            values="Count",
            hole=0.55,
            template="plotly_dark"
        )

        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Detection Pipeline")

    st.info(
        "Email Input → Text Preprocessing → TF-IDF "
        "→ Machine Learning Classification → Prediction"
    )

    st.caption(
        "Statistics are from the original project dataset and "
        "held-out test results, not live scan counts."
    )


# ==========================================
# PAGE 2: EMAIL SCANNER
# ==========================================

elif page == "Email Scanner":

    st.subheader("📨 Email Threat Scanner")

    st.write(
        "Paste an email below to analyse it using "
        "your trained machine learning classifiers."
    )

    if not models_loaded:
        st.error("Trained models could not be loaded.")
        st.stop()

    selected_model = st.selectbox(
        "Select Classification Model",
        list(models.keys())
    )

    email_text = st.text_area(
        "Email Content",
        height=220,
        placeholder="Paste email subject and body here..."
    )

    if st.button("🔍 SCAN EMAIL", use_container_width=True):

        if not email_text.strip():

            st.warning("Please enter email content.")

        else:

            try:

                features = vectorizer.transform([email_text])

                model = models[selected_model]

                prediction = int(model.predict(features)[0])

                st.divider()

                if prediction == 1:

                    st.error("🚨 PHISHING EMAIL DETECTED")

                    st.subheader("⚠️ High Risk Classification")

                    st.write(
                        "The model classified this email "
                        "as a potential phishing attempt."
                    )

                else:

                    st.success("✅ EMAIL CLASSIFIED AS LEGITIMATE")

                    st.subheader("No phishing pattern detected")

                    st.write(
                        "The model classified this email as legitimate. "
                        "This does not guarantee that it is safe."
                    )

                if hasattr(model, "predict_proba"):

                    probabilities = model.predict_proba(features)[0]

                    classes = list(model.classes_)

                    phishing_index = classes.index(1)

                    phishing_probability = (
                        probabilities[phishing_index] * 100
                    )

                    st.metric(
                        "Model Phishing Probability",
                        f"{phishing_probability:.2f}%"
                    )

                    st.progress(
                        int(round(phishing_probability))
                    )

                    st.caption(
                        "Model probability estimate, not a calibrated "
                        "guarantee of real-world risk."
                    )

                st.caption(
                    f"Model: {selected_model} | Prediction: {prediction}"
                )

            except Exception as e:

                st.error(f"Prediction failed: {e}")

    st.divider()

    st.subheader("Try Sample Emails")

    with st.expander("Sample 1 - Phishing Email"):

        st.code("""
Subject: URGENT: Account Verification Required

Dear Customer,

Your bank account has been temporarily suspended
due to unusual activity.

Verify your account immediately by clicking the
link below and entering your banking credentials.

Failure to verify within 24 hours may result in
permanent account suspension.

Regards,
Online Banking Security Team
        """)

    with st.expander("Sample 2 - Legitimate Email"):

        st.code("""
Subject: Project Meeting - Updated Schedule

Hi Team,

I hope everyone is doing well.

This is a reminder that our project meeting
has been rescheduled to Thursday at 11 AM.

Please review the shared presentation before
the meeting.

Regards,
Project Coordinator
        """)


# ==========================================
# PAGE 3: MODEL ANALYTICS
# ==========================================

elif page == "Model Analytics":

    st.subheader("📊 Model Performance Analytics")

    st.caption(
        "Original held-out test set: 16,498 emails."
    )

    st.dataframe(
        results.style.format({
            "Accuracy": "{:.4f}%"
        }),
        use_container_width=True,
        hide_index=True
    )

    st.subheader("Accuracy Comparison")

    fig = px.bar(
        results,
        x="Model",
        y="Accuracy",
        color="Model",
        text="Accuracy",
        template="plotly_dark"
    )

    fig.update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside"
    )

    fig.update_layout(
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Confusion Matrix Analysis")

    selected = st.selectbox(
        "Choose Model",
        list(confusion_matrices.keys())
    )

    cm = np.array(confusion_matrices[selected])

    fig, ax = plt.subplots(figsize=(6, 4))

    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=["Legitimate", "Phishing"]
    )

    disp.plot(
        ax=ax,
        cmap="Blues",
        colorbar=False,
        values_format="d"
    )

    ax.set_title(selected)

    fig.tight_layout()

    st.pyplot(fig)

    plt.close(fig)

    st.markdown("""
    **Confusion Matrix Terms**

    - TN: Legitimate emails correctly identified.
    - FP: Legitimate emails incorrectly flagged.
    - FN: Phishing emails missed by the model.
    - TP: Phishing emails correctly identified.
    """)

    st.info(
        "Random Forest achieved the highest reported "
        "test accuracy of 98.7150%."
    )


# ==========================================
# PAGE 4: ABOUT PROJECT
# ==========================================

elif page == "About Project":

    st.subheader("About PhishSense")

    st.write("""
    PhishSense is an AI-driven phishing email detection
    system developed using Natural Language Processing
    and supervised Machine Learning algorithms.

    It analyses email text and predicts whether
    the content is phishing or legitimate.
    """)

    st.divider()

    st.subheader("Dataset Information")

    st.markdown("""
    - Total samples: 82,486
    - Phishing samples: 42,891
    - Legitimate samples: 39,595
    - Train-test split: Stratified 80:20
    - Sources: Enron, Ling, Nazario, Nigerian Fraud,
      CEAS and SpamAssassin.
    """)

    st.divider()

    st.subheader("Methodology")

    st.markdown("""
    1. Dataset loading and text preparation.
    2. TF-IDF feature extraction.
    3. Stratified train-test split.
    4. Training four supervised classifiers.
    5. Evaluation using accuracy and confusion matrices.
    """)

    st.divider()

    st.subheader("Technologies Used")

    st.write("""
    Python · Pandas · Scikit-learn · TF-IDF ·
    Streamlit · Plotly · Matplotlib · Joblib
    """)

    st.divider()

    st.subheader("Limitations")

    st.warning("""
    The system analyses email text only.

    It does not verify sender identity, SPF/DKIM
    authentication, URL reputation or attachments.

    A legitimate classification is not a guarantee
    that an email is safe.
    """)

    st.markdown(
        "[Dataset Source: Kaggle](https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset)"
    )


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "PhishSense | AI-Powered Email Threat Detection"
)
