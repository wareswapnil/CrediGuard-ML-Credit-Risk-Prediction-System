# 🛡️ CrediGuard ML – Credit Risk Prediction System

## 🚀 Overview

CrediGuard ML is a Machine Learning-powered web application that predicts whether a loan applicant is a **Good** or **Bad credit risk** based on financial and personal attributes.

The system helps financial institutions make smarter lending decisions by analyzing applicant data and reducing default risk.

---

## 🎯 Features

* 🔍 Predicts credit risk (Good / Bad)
* 📊 Uses Machine Learning (Extra Trees Classifier)
* ⚡ Real-time prediction using Streamlit UI
* 🧠 Handles categorical data using encoding
* 📈 Displays prediction instantly with user input

---

## 🛠️ Tech Stack

* Python 🐍
* Pandas & NumPy
* Scikit-learn
* Joblib (model persistence)
* Streamlit (web app)

---

## 📂 Project Structure

```
CrediGuard-ML-Credit-Risk-Prediction-System/
│── app.py
│── extra_trees_credit_model.pkl
│── Sex_encoder.pkl
│── Housing_encoder.pkl
│── Saving_accounts_encoder.pkl
│── Checking_account_encoder.pkl
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/wareswapnil/CrediGuard-ML-Credit-Risk-Prediction-System.git
cd CrediGuard-ML-Credit-Risk-Prediction-System
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Application

```bash
streamlit run app.py
```
deploy 
https://crediguard-ml-credit-risk-prediction-system-mnv3yntjhpqsa9iqly.streamlit.app/
---

## 🧪 Input Parameters

* Age
* Sex
* Job
* Housing
* Saving Accounts
* Checking Account
* Credit Amount
* Duration

---

## 📊 Output

* ✅ Good Credit Risk
* ❌ Bad Credit Risk

---

## 🧠 Machine Learning Model

* Model Used: **Extra Trees Classifier**
* Trained on German Credit Dataset
* Feature Encoding: Label Encoding
* Evaluation Metrics: Accuracy, Cross-validation

---

## 📸 Demo

(Add screenshots here after running app)
<img width="1827" height="850" alt="Screenshot 2026-04-01 231156" src="https://github.com/user-attachments/assets/2346212f-4ef2-425a-9214-a8b3e00bcbca" />

<img width="1723" height="853" alt="Screenshot 2026-04-01 231211" src="https://github.com/user-attachments/assets/a2b8fef3-7b00-4a83-ad62-c82a73675668" />


## 🌐 Future Improvements

* 📊 Add probability score visualization
* 🎨 Improve UI/UX design
* ☁️ Deploy on Streamlit Cloud
* 🔍 Add feature importance visualization

---

## 👨‍💻 Author

Swapnil Ware
Final Year IT Student (2026)

---

## ⭐ If you like this project, give it a star!
