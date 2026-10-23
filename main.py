from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app = FastAPI()
class res(BaseModel):
    name:str
    age:int
@app.get("/user/{user_id}",response_model=res)
def home(user_id:int):
    if user_id!=1:
        raise HTTPException(
            status_code=404,
            detail='no such user found'
        )
        
    return {'name':'mohit',
            'age':24,
            'password':'1234'}