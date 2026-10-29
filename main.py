from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker
from fastapi import FastAPI

app = FastAPI()

engine = create_engine(
    "sqlite:///test.db",
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    completed = Column(Boolean, default=False)


Base.metadata.create_all(bind=engine)
@app.get('/')
def home():
    return {'home':'message'}