from fastapi import FastAPI
from datetime import datetime, timedelta
from pydantic import EmailStr

# -------------------------------------------------------------------------------------------------

app = FastAPI()
lst = {}


# -------------------------------------------------------------------------------------------------
@app.post("/data")
def post_data(sender_email_address: EmailStr, reciver_email_address: EmailStr, title: str, text: str):
    time_sent = datetime.utcnow()
    lst[reciver_email_address] = [sender_email_address, title, text, time_sent]
    return {"status:The Email sent"}


# -------------------------------------------------------------------------------------------------
@app.get("/inbox")
def get_data(reciver_email_address: str):
    return lst[reciver_email_address]
