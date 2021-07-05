"""
The code created by liberty on 7/5/21

"""
from celery import shared_task


@shared_task
def func_add(x, y):
    return x + y
