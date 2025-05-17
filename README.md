# 🔐 URL Spam Detection using Machine Learning Pipelines

This project is a **network security solution** designed to detect whether a given URL is **spam (malicious)** or **ham (safe)** using end-to-end machine learning pipelines. It is structured around modular and maintainable components for data ingestion, validation, transformation, and model training.

---

## 📌 Overview

Malicious URLs are a common method used in phishing and other cyber attacks. This project uses traditional machine learning techniques to automatically detect such threats and classify URLs as either spam or ham.

The system is built using a clean pipeline architecture, making it scalable and suitable for deployment or further research.

---

## 🔄 ML Pipeline Components

1. **Data Ingestion**  
   - Loads raw URL data from source files (e.g., CSV)
   - Splits data into training and testing sets
   - Stores ingested data in structured directories

2. **Data Validation**  
   - Checks for missing values and data format issues
   - Logs and reports any inconsistencies

3. **Data Transformation**  
   - Extracts features such as URL length, special character counts, presence of keywords (e.g., `login`, `verify`)
   - Normalizes and prepares data for modeling

4. **Model Training**  
   - Trains a classifier (e.g., Random Forest, Logistic Regression)
   - Evaluates on test data
   - Saves the model and performance metrics

---

## 🧠 Features Extracted from URLs

- URL length  
- Count of special characters (`.`, `/`, `-`, `@`, etc.)  
- Use of HTTPS or IP addresses  
- Presence of suspicious keywords (`free`, `login`, `secure`, etc.)

---

## 🛠 Technologies Used

- **Python** (3.x)
- **scikit-learn** – ML modeling
- **pandas** – Data manipulation
- **joblib / pickle** – Model serialization
- **os / logging / yaml** – For configuration and logging

---

## 🚀 Features

- ✅ Modular ML pipeline:
  - **Data Ingestion**
  - **Data Validation**
  - **Data Transformation**
  - **Model Training & Evaluation**
- ✅ **Batch prediction** support (`batch_prediction.py`)
- ✅ **Streamlit UI** for real-time URL checks (`streamlit_app.py`)
- ✅ **MongoDB integration** (optional, see `test_mongo.py`)
- ✅ Logs and exception handling
- ✅ Docker-compatible
