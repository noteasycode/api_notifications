from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from .models import Notification


@shared_task()
def send_email(notification_id):
    notification = Notification.objects.get(id=notification_id)
    subject = f'{notification.name}'
    message = f'{notification.text}.'
    mail_sent = send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[notification.receiver.email]
    )
    return mail_sent
