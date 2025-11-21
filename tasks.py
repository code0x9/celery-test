from celery import Celery
from _types import AddableT

app = Celery("tasks")


@app.task
def add(x: AddableT, y: AddableT) -> AddableT:
    return x + y
