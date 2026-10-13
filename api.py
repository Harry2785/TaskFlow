from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from task_service import (
    get_tasks,
    get_task,
    add_task,
    delete_task,
    complete_task
)


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Task(BaseModel):
    id: int
    name: str
    completed: bool


class TaskCreate(BaseModel):
    name: str


@app.get("/")
def home():
    return {"message": "Welcome to TaskFlow API"}


@app.get("/tasks")
def get_all_tasks():

    tasks = get_tasks()

    result = []

    for task in tasks:

        task_id, name, completed = task

        result.append(
            Task(
                id=task_id,
                name=name,
                completed=bool(completed)
            )
        )

    return result


@app.post("/tasks")
def create_task(task: TaskCreate):

    task_id = add_task(task.name)

    return Task(
        id=task_id,
        name=task.name,
        completed=False
    )

@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):

    task = get_task(task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    delete_task(task_id)

    return {"message": "Task deleted successfully"}


@app.patch("/tasks/{task_id}")
def mark_task_complete(task_id: int):

    task = get_task(task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    complete_task(task_id)

    return {"message": "Task completed successfully"}