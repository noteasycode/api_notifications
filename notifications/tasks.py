from celery import shared_task

from .models import Notification


@shared_task()
def send_email():
    return None
