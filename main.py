from fastapi import FastAPI,middleware,Request
import time
app = FastAPI()
@app.middleware('http')
async def my_midd(req:Request,call_next):
    start_time=time.time()
    print(start_time)
    res=await call_next(req)
    end_time=time.time()
    print(end_time)
    return res
# @app.middleware('http')
# async def my_middleware(request:Request,call_next):
#     print('req recived')
#     response=await call_next(request)
#     print('respose sent')
#     return response
        
@app.get("/")
def home():
    return {'name':'mohit',
            'age':24,
            'password':'1234'}