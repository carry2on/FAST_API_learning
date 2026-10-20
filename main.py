from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id: int
    title: str
    completed: bool

@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {
        "message": "Todo added",
        "data": todos
    }
@app.get("/todos")
def get_todos():
    return todos
  
@app.get('/todos/{todo_id}')
def todospecific(todo_id:int):
  for t in todos:
    if t.id==todo_id:
      return t
  return {'error':'no such id data avalible'}
from fastapi import HTTPException

# PUT - Update Todo
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, t in enumerate(todos):
        if t.id == todo_id:
            todos[index] = updated_todo
            return {
                "message": "Todo updated",
                "data": updated_todo
            }

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )


# DELETE - Delete Todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for t in todos:
        if t.id == todo_id:
            todos.remove(t)
            return {"message": "Todo deleted"}

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )