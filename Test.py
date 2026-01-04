from fastapi import FastAPI
from pydantic import BaseModel


class Num(BaseModel):
    number : int
app = FastAPI()
@app.post("/user")
def create_user(num: Num):
    return num

