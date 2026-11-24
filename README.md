# 🛡️ PhishSense
### AI-Powered Phishing Email Detection System

**Detect suspicious emails. Identify potential threats. Stay one step ahead.**

PhishSense is a machine learning-based phishing email detection system that analyses email content and classifies it as either **Phishing** or **Legitimate** using Natural Language Processing (NLP) and supervised machine learning algorithms.

The project implements TF-IDF feature extraction and compares four machine learning classifiers to identify the most effective model for phishing email detection.

---

## ✨ Key Features

- **Email Classification:** Analyse email text and identify potential phishing attempts.
- **Multiple ML Models:** Compare four trained machine learning classifiers.
- **TF-IDF Vectorization:** Convert raw email text into numerical features for classification.
- **Interactive Dashboard:** Explore model performance and dataset statistics through a Streamlit interface.
- **Live Email Scanning:** Paste email content and receive an instant model prediction.
- **Model Analytics:** Visualize accuracy comparisons and confusion matrices.
- **Probability Estimates:** View the model's estimated phishing probability where supported.

---

## 🧠 Machine Learning Models

PhishSense implements and evaluates four supervised learning algorithms:

| Model | Accuracy |
|---|---:|
| Random Forest | **98.71%** |
| MLP Classifier | 98.43% |
| Logistic Regression | 98.38% |
| Multinomial Naive Bayes | 96.00% |

Random Forest achieved the highest accuracy among the four evaluated classifiers.

*Results are based on the project's original 80:20 stratified train-test split.*

---

## 📊 Dataset

The project uses the [Phishing Email Dataset](https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset) available on Kaggle.

The primary dataset used for model training is `phishing_email.csv`.

### Dataset Statistics

| Category | Count |
|---|---:|
| Total Emails | 82,486 |
| Phishing Emails (Label 1) | 42,891 |
| Legitimate Emails (Label 0) | 39,595 |

The dataset contains email samples from multiple sources, including Enron, Ling, Nazario, Nigerian Fraud, CEAS and SpamAssassin.

---

## ⚙️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation and preprocessing |
| Scikit-learn | Machine learning and evaluation |
| TF-IDF | Text feature extraction |
| Streamlit | Interactive dashboard |
| Plotly | Interactive visualizations |
| Matplotlib | Confusion matrix visualization |
| Joblib | Model serialization and loading |
| KaggleHub | Dataset acquisition |

---

## 🔬 Methodology

The project follows the following machine learning pipeline:

1. **Dataset Acquisition:** Download and load the phishing email dataset.
2. **Data Preparation:** Extract email text and classification labels.
3. **Train-Test Split:** Divide the dataset into training and testing subsets using an 80:20 stratified split.
4. **Feature Extraction:** Apply TF-IDF vectorization with:
   - Maximum features: 10,000
   - Stop words: English
   - N-gram range: (1, 2)
5. **Model Training:** Train four supervised classification algorithms.
6. **Model Evaluation:** Evaluate performance using accuracy, precision, recall, F1-score and confusion matrices.
7. **Model Serialization:** Save trained models and the TF-IDF vectorizer using Joblib.
8. **Dashboard Integration:** Integrate the saved models into a Streamlit dashboard for interactive email classification.

---

## 📈 Model Evaluation

The models were evaluated on a held-out test set containing 16,498 email samples.

### Random Forest Confusion Matrix

| | Predicted Legitimate | Predicted Phishing |
|---|---:|---:|
| Actual Legitimate | 7,810 | 109 |
| Actual Phishing | 103 | 8,476 |

### Random Forest Performance

- **Accuracy:** 98.71%
- **Precision:** Approximately 98.73%
- **Recall:** Approximately 98.80%
- **F1-score:** Approximately 98.77%

These precision, recall and F1-score values are derived from the reported confusion matrix.

---

## 🖥️ Dashboard

PhishSense provides an interactive dashboard with four main sections:

### 1. Overview
- Dataset statistics
- Model accuracy comparison
- Dataset class distribution
- Detection pipeline

### 2. Email Scanner
- Paste email content
- Select a classification model
- Scan and classify emails
- View phishing probability estimates

### 3. Model Analytics
- Model accuracy comparison
- Confusion matrix visualization
- Performance evaluation

### 4. About Project
- Dataset information
- Project methodology
- Technology stack
- System limitations

---

## 🚀 Installation and Setup

### Prerequisites

- Python 3.10 or later
- VS Code (recommended)
- pip package manager

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/PhishSense.git
cd PhishSense
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it:

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare Model Files

Ensure the following trained model files are present inside the `models/` directory:

```text
models/
├── tfidf_vectorizer.joblib
├── logistic_regression.joblib
├── random_forest.joblib
├── naive_bayes.joblib
└── mlp.joblib
```

These files are generated by the model training notebook.

### 5. Run the Application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal, usually:

```text
http://localhost:8501
```

---

## 📁 Project Structure

```text
PhishSense/
│
├── models/
│   ├── tfidf_vectorizer.joblib
│   ├── logistic_regression.joblib
│   ├── random_forest.joblib
│   ├── naive_bayes.joblib
│   └── mlp.joblib
│
├── notebook.ipynb
│
├── app.py
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

## 🔮 Future Improvements

Potential extensions to PhishSense include:

- URL extraction and reputation analysis.
- Sender domain and email authentication checks.
- Detection of suspicious attachments.
- Integration of deep learning and transformer-based NLP models.
- Real-time phishing threat intelligence.
- Email header analysis.
- Enhanced explainability to identify suspicious phrases and patterns.
- Deployment through a cloud hosting platform.

---

## ⚠️ Limitations

PhishSense currently analyses email text using trained machine learning classifiers.

It does not independently verify sender identity, SPF/DKIM authentication, URL reputation, attachments or live website safety.

A legitimate prediction does not guarantee that an email is safe. The system is intended as a research and educational demonstration, not a replacement for professional email security solutions.

---

## 👩‍💻 Created By

**Aarushi Singh**

Developer of **PhishSense – AI-Powered Phishing Email Detection System**.

This project explores the application of Natural Language Processing and machine learning techniques to cybersecurity, with a focus on identifying and classifying phishing emails.

---

## 📌 Project Information

| Detail | Description |
|---|---|
| Project Name | PhishSense |
| Domain | Machine Learning, NLP & Cybersecurity |
| Language | Python |
| Interface | Streamlit |
| Classification | Binary Classification |
| Models | Random Forest, Logistic Regression, Multinomial Naive Bayes, MLP |

---

<p align="center">
  <strong>PhishSense</strong><br>
  Made with ❤️ by Aarushi Singh
</p>

<p align="center">
  <em>Building smarter solutions for a safer digital world.</em> 🛡️
</p>
