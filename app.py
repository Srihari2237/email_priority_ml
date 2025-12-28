import streamlit as st
import joblib
from feedback import save_feedback, retrain_model

model = joblib.load("model/classifier.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

st.title("Email Priority Classifier")

email_text = st.text_area("Enter email text:")

if st.button("Predict"):
    X = vectorizer.transform([email_text])
    prediction = model.predict(X)[0]
    st.success(f"Predicted Priority: {prediction}")

    st.write("Is this correct?")
    col1, col2, col3 = st.columns(3)

    if col1.button("High"):
        save_feedback(email_text, "High")
        retrain_model()
        st.info("Feedback saved and model updated.")

    if col2.button("Medium"):
        save_feedback(email_text, "Medium")
        retrain_model()
        st.info("Feedback saved and model updated.")

    if col3.button("Low"):
        save_feedback(email_text, "Low")
        retrain_model()
        st.info("Feedback saved and model updated.")
