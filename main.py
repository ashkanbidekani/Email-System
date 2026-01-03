from fastapi import FastAPI
app = FastAPI()

# -------------------------------
mailbox = {}

# -------------------------------
@app.post("/send-email")
def send_email(sender_email: str,receiver_email: str,subject: str,text: str):
    email_data = {
        "from": sender_email,
        "subject": subject,
        "text": text
    }

    if receiver_email not in mailbox:
        mailbox[receiver_email] = []

    mailbox[receiver_email].append(email_data)

    return {"status": "Email sent successfully"}

# -------------------------------
@app.get("/inbox")
def get_inbox(email: str):
    if email not in mailbox:
        return {"emails": []}

    return {"emails": mailbox[email]}
