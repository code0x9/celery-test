from celery import Celery
from _types import AddableT

app = Celery(
    "tasks", backend="redis://localhost:6379/0", broker="redis://localhost:6379/0"
)


@app.task
def add(x: AddableT, y: AddableT) -> AddableT:
    return x + y
