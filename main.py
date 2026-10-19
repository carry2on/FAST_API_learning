from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}
@app.get("/products")
def home(limit:int=10,name:str='laptop'):
    return {"message": limit}