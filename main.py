import sqlite3
from fastapi import FastAPI
conn=sqlite3.connect('test.db',check_same_thread=False)
cursor=conn.cursor()
cursor.execute("""
               CREATE TABLE IF NOT EXISTS todos(
                   id INTEGER PRIMARY KEY,
                   title TEXT,
                   completed TEXT
                   
               )
               """)
conn.commit()
app=FastAPI()
@app.get('/')
def home():
    return {'sql is connected sucess fully'}