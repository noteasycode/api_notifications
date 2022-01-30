from django import forms
from django.forms import DateTimeField, Textarea
from django.contrib.admin.widgets import AdminSplitDateTime

from .models import Notification


class NotificationForm(forms.ModelForm):
    notify_date = forms.SplitDateTimeField(widget=AdminSplitDateTime())

    class Meta:
        model = Notification
        fields = ('name', 'text', 'notify_date')
        labels = {
            'name': ('Name'),
            'text': ('Description'),
            'notify_date': ('When you want to recieve notification?'),
        }
        widgets = {
            'text': Textarea(attrs={"class": "form-control"}),
        }
