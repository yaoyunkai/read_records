"""
The code created by liberty on 7/3/21

"""
from .celery import app


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y
