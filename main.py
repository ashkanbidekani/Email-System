from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from datetime import datetime,timedelta
app = FastAPI()

# -------------------------------
mailbox = {}


# -------------------------------
class Email(BaseModel):

    sender_email: EmailStr
    receiver_email: EmailStr
    subject: str
    text: str
    current_time: float

# -------------------------------
@app.post("/send-email")
def send_email(email: Email):
    email_data = {
        "from": email.sender_email,
        "subject": email.subject,
        "text": email.text,
        "current_time" : datetime.utcnow()
    }
    current_time = datetime.utcnow()

    if email.receiver_email not in mailbox:
        mailbox[email.receiver_email] = []

    mailbox[email.receiver_email].append(email_data)

    return {"status": "Email sent successfully"}


# -------------------------------
@app.get("/inbox")
def get_inbox(email: EmailStr):
    if email not in mailbox:
        return {"emails": []}

    return {"emails": mailbox[email]}
