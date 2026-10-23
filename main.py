from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class User(BaseModel):
    name:str
    age:int
    password:str
    
class Userresponse(BaseModel):
    name:str
    age:int
@app.get("/",response_model=Userresponse)
def home():
    return {'name':'mohit',
            'age':24,
            'password':'1234'}