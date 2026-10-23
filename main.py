from fastapi import FastAPI,status,HTTPException

app = FastAPI()

@app.get("/",status_code=status.HTTP_201_CREATED)
def home():
    return {"message": "Hello World"}
@app.get('/users/{user_id}')
def get_user(user_id:int):
    
    if user_id!=1:
        return HTTPException(
            status_code=404,
            detail='user not found'
        )
    return{
        'id':1,
        'name':'manank'
    }