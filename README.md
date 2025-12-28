# Email Priority Classifier with Feedback Loop

## Overview
This project is an end-to-end NLP-based machine learning application that classifies emails into High, Medium, or Low priority. It continuously improves using user feedback.

## Features
- TF-IDF text vectorization
- Logistic Regression classifier
- Human-in-the-loop learning
- Streamlit web application
- Automatic retraining

## How to Run

```bash
pip install -r requirements.txt
python generate_data.py
python train.py
streamlit run app.py
