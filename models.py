from pydantic import BaseModel
from typing import Optional


class TodoModel(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    completed: bool = False


class TodoUpdateModel(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
