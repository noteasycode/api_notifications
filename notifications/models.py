from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)


class Notification(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    notify_date = models.DateTimeField()
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')

    class Meta:
        ordering = ['-notify_date']

    def __str__(self):
        return self.name
