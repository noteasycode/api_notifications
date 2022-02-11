from django.contrib import admin
from django.contrib.auth import get_user_model

from notifications.models import Notification


CustomUser = get_user_model()


class AccountAdminArea(admin.AdminSite):
    site_header = 'Accounts'


class NotificationAdminPermission(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return True


class CustomUserAdminPermission(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        return True


accounts_site = AccountAdminArea(name='AccountAdmin')

accounts_site.register(CustomUser, CustomUserAdminPermission)
accounts_site.register(Notification, NotificationAdminPermission)
