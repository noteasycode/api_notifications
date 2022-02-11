from django.contrib import admin
from django.contrib.auth import get_user_model

from notifications.models import Notification


CustomUser = get_user_model()


class AccountAdminArea(admin.AdminSite):
    site_header = 'Accounts'


accounts_site = AccountAdminArea(name='AccountAdmin')

accounts_site.register(CustomUser)
accounts_site.register(Notification)
