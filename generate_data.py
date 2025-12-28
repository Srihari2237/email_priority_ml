import pandas as pd
import random

high_priority = [
    "Urgent payment required",
    "Immediate action needed for security update",
    "Project deadline tomorrow",
    "Invoice overdue please respond",
]

medium_priority = [
    "Weekly team meeting schedule",
    "Please review the attached document",
    "Client feedback on last delivery",
]

low_priority = [
    "Big sale this weekend",
    "Subscribe to our newsletter",
    "Limited time promotional offer",
]

data = []

for _ in range(100):
    data.append((random.choice(high_priority), "High"))
    data.append((random.choice(medium_priority), "Medium"))
    data.append((random.choice(low_priority), "Low"))

df = pd.DataFrame(data, columns=["text", "priority"])
df.to_csv("data/initial_emails.csv", index=False)

print("Dataset generated successfully.")
