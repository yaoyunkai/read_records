"""
The code created by liberty on 7/3/21

"""

import os

from celery import Celery
from kombu import Queue

base_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(base_dir)
demo_file_path = os.path.join(base_dir, 'demo.txt')

app = Celery(
    'core',
    broker='amqp://admin:admin@localhost:5672/',
    backend='redis://localhost:6379/0',
    include=['core.tasks']
)

# app.conf.beat_schedule = {
#     'add-every-30-seconds': {
#         'task': 'core.tasks.add',
#         'schedule': 30.0,
#         'args': (16, 16)
#     },
# }

app.conf.timezone = 'UTC'


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    # sender.add_periodic_task(
    #     crontab(hour=7, minute=30, day_of_week=1),
    #     test.s('Happy Mondays!'),
    # )


app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'core.celery.func_add',
        'schedule': 30.0,
        'args': (16, 16)
    },
}

app.conf.timezone = 'UTC'

app.conf.task_default_queue = 'default'

app.conf.task_queues = (
    Queue('default', routing_key='task.#'),
    Queue('feed_tasks', routing_key='feed.#'),
)

app.conf.task_default_exchange = 'tasks'
app.conf.task_default_exchange_type = 'topic'
app.conf.task_default_routing_key = 'task.default'


@app.task(bind=True)
def test(self, arg):
    f = open(demo_file_path, mode='a')
    f.write('exec task, arg: {}\n'.format(arg))
    f.close()


@app.task
def func_add(x, y):
    return x + y


if __name__ == '__main__':
    app.start()
