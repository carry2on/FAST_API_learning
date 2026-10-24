from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {'name':'mohit',
            'age':24,
            'password':'1234'}