import imaplib
import email
import joblib
from email_config import EMAIL_ADDRESS, EMAIL_PASSWORD, IMAP_SERVER, IMAP_PORT
if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
    raise RuntimeError("EMAIL_ADDRESS or EMAIL_PASSWORD environment variable not set")

# Load trained ML components
model = joblib.load("../model/classifier.pkl")
vectorizer = joblib.load("../model/vectorizer.pkl")


def clean_email_body(msg):
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                return part.get_payload(decode=True).decode(errors="ignore")
    else:
        return msg.get_payload(decode=True).decode(errors="ignore")
    return ""


def fetch_and_classify_emails():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    mail.select("inbox")

    status, messages = mail.search(None, "UNSEEN")
    email_ids = messages[0].split()

    print(f"Unread emails found: {len(email_ids)}")

    for e_id in email_ids[::-1]:  
        _, msg_data = mail.fetch(e_id, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])

        subject = msg["subject"] or ""
        date = msg["date"] or "Unknown date"
        body = clean_email_body(msg)

        text = subject + " " + body
        X = vectorizer.transform([text])
        prediction = model.predict(X)[0]

        print("-" * 50)
        print(f"Date: {date}")
        print(f"Subject: {subject}")
        print(f"Predicted Priority: {prediction}")

    mail.logout()


if __name__ == "__main__":
    fetch_and_classify_emails()
