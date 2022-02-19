from django.db import models
from django.conf import settings


class Notification(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    notify_date = models.DateTimeField()
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    celery_task_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['notify_date']

    def __str__(self):
        return self.name
