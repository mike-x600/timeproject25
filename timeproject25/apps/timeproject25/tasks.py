from celery import shared_task
from timeproject25.celery import app as celery_app 
from celery.exceptions import SoftTimeLimitExceeded

@shared_task
def add(x, y):
    print("shared_task::add")
    return x + y


@celery_app.task
def mytask():
    try:
        print("mytask")
    except SoftTimeLimitExceeded:
        print("limit done")
    return True


@celery_app.task(bind=True, ignore_result=True)
def debug_task(self):
    print("@app.task::debug_task")
    print(f'Request: {self.request!r}')