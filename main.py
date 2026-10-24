
from fastapi import FastAPI, Depends,Header,HTTPException

app = FastAPI()
def varify_token(token:str=Header(None)):
    if token!='mysecrettoken':
        raise HTTPException(status_code=401,detail='unauthorized')
# def common_logic():
#     return {"message": "common logic executed"}

# @app.get("/home")
# def home(data = Depends(common_logic)):
#     return data

@app.get('/secure_data')
def secure_data(user=Depends(varify_token)):
    return user