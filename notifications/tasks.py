from celery import shared_task
from django.core.mail import send_mail

from .models import Notification


@shared_task()
def send_email(notification_id):
    notification = Notification.objects.get(id=notification_id)
    subject = f''
    mail_sent = send_mail(subject, )
    return mail_sent
