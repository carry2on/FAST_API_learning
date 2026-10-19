from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}
#three topics 
# querystring making
# validation and the defaul valuse in the qepara
# multiple para
@app.get("/products")
def home(limit:int=10,name:str='laptop'):
    return {"message": limit,
            'name':name}