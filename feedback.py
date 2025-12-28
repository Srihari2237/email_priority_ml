import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression

def save_feedback(text, correct_label):
    try:
        df = pd.read_csv("data/feedback.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["text", "priority"])

    df = pd.concat([df, pd.DataFrame([[text, correct_label]], columns=df.columns)])
    df.to_csv("data/feedback.csv", index=False)

def retrain_model():
    base = pd.read_csv("data/initial_emails.csv")
    try:
        feedback = pd.read_csv("data/feedback.csv")
        df = pd.concat([base, feedback])
    except FileNotFoundError:
        df = base

    vectorizer = joblib.load("model/vectorizer.pkl")
    X = vectorizer.fit_transform(df["text"])
    y = df["priority"]

    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)

    joblib.dump(model, "model/classifier.pkl")
    joblib.dump(vectorizer, "model/vectorizer.pkl")
