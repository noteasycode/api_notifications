import datetime
from django.contrib.auth import get_user_model
from django.test import TestCase

from notifications.models import Notification

User = get_user_model()


class NotificationModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.notification_1 = Notification.objects.create(
            name='Test notification',
            text='Test notification text',
            notify_date=datetime.datetime.now(datetime.timezone.utc),
            receiver=User.objects.create_user(username='TestUser')
        )

    def test_object_name_is_text_field(self):
        notification = NotificationModelTest.notification_1
        expected_object_name = notification.name
        self.assertEqual(expected_object_name, str(notification))

