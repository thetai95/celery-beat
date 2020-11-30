from celery import shared_task
from time import sleep
from datetime import datetime


@shared_task(bind=True)
def go_to_sleep(self, duration):
    sleep(duration)
    return "Done!"


@shared_task(bind=True)
def get_current_time(self):
    return datetime.now().strftime("%H:%M:%S")
