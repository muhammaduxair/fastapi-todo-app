from fastapi import APIRouter, HTTPException
from models import TodoModel, TodoUpdateModel

# define a router
router = APIRouter(prefix='/api/v1/todo')

# dummy list of todo
todos: list[TodoModel] = []


@router.post('/', response_model=TodoModel)
def create_todo(todo: TodoModel):
    todo.id = len(todos) + 1
    todos.append(todo)
    return todo


@router.get('/', response_model=list[TodoModel])
def get_todos(search: str = None):
    if search is None:
        return todos
    return [t for t in todos if search.lower() in t.title.lower() or search.lower() in t.description.lower()]


@router.get('/{todo_id}', response_model=TodoModel)
def get_todo_by_id(todo_id: int):
    item = next((t for t in todos if t.id == todo_id), None)
    if item:
        return item
    else:
        raise HTTPException(status_code=404, detail="Item not found")


@router.put('/{todo_id}', response_model=TodoModel)
def update_todo_by_id(todo_id: int, todo: TodoUpdateModel):
    item = next((t for t in todos if t.id == todo_id), None)

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    # Update fields only if they have new values
    update_data = todo.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(item, field, value)

    return item


@router.delete("/{todo_id}", response_model=dict)
def delete_todo_by_id(todo_id: int):
    item = next((t for t in todos if t.id == todo_id), None)

    if not item:
        raise HTTPException(
            status_code=404, detail="Item not found")

    todos.remove(item)
    return {"message": f"Todo item with ID {todo_id} deleted successfully"}
