from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Notification(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    notify_date = models.DateTimeField()

    class Meta:
        ordering = ['-notify_date']

    def __str__(self):
        return self.name
