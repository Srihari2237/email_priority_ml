import os
from dotenv import load_dotenv

load_dotenv()  # loads .env file

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

IMAP_SERVER = "imap.gmail.com"
IMAP_PORT = 993
