from celery import Celery
from typing import TypeVar

T = TypeVar('T', str, int, float, list, tuple)

app = Celery('tasks', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')

@app.task
def add(x: T, y: T) -> T:
    return x + y
