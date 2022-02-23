import datetime
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from notifications.models import Notification

User = get_user_model()


class NotificationURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.notification = Notification.objects.create(
            name='Test notification',
            text='Test notification text',
            notify_date=datetime.datetime.now(datetime.timezone.utc),
            receiver=User.objects.create_user(username='test_user')
        )

    def setUp(self):
        self.guest_client = Client()
        self.user = NotificationURLTests.notification.receiver
        self.not_author = User.objects.create_user(username='not_author')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)
        self.not_author_client = Client()
        self.not_author_client.force_login(self.not_author)

    def test_urls_uses_correct_template(self):
        templates_url_names = {
            reverse('notifications:index'): 'index.html',
            reverse('notifications:notifications_list', kwargs={
                'username': NotificationURLTests.notification.receiver
            }): 'notifications_list.html',
            reverse('notifications:new_notification'): 'new.html',
            reverse('notifications:edit', kwargs={
                'username': NotificationURLTests.notification.receiver,
                'pk': NotificationURLTests.notification.pk
            }): 'new.html',
        }
        for adress, template in templates_url_names.items():
            with self.subTest(adress=adress):
                response = self.authorized_client.get(adress)
                self.assertTemplateUsed(response, template)

        for adress in templates_url_names.keys():
            with self.subTest(adress=adress):
                response = self.authorized_client.get(adress)
                self.assertEqual(response.status_code, 200)

        for adress in templates_url_names.keys():
            with self.subTest(adress=adress):
                response = self.guest_client.get(adress)
                if adress == '/':
                    self.assertEqual(response.status_code, 200)
                else:
                    self.assertEqual(response.status_code, 302)