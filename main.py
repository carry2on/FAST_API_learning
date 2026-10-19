from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
# 1
# # json input handling
# # post req
# # intro to pydantic
# class User(BaseModel):
#     name: str
#     age: int
#     email: str


# @app.post("/create-user")
# def create_user(user: User):
#     return {
#         "message": "User created",
#         "data": user
#     }

#2

# class Address(BaseModel):
#     city:str
#     pincode:int
# class  User(BaseModel):
#     name:str
#     age:int
#     address:Address  # connect the address modesl at above in there
# @app.post("/create-user")
# def create_user(user: User):
#     return user