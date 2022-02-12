from django.contrib import admin
from django.contrib.auth import get_user_model

from notifications.models import Notification


CustomUser = get_user_model()


@admin.action(description='Block selected users')
def block_user(modeladmin, request, queryset):
    queryset.update(is_active='False')


@admin.action(description='Unblock selected users')
def unblock_user(modeladmin, request, queryset):
    queryset.update(is_active='True')


class AccountAdminArea(admin.AdminSite):
    site_header = 'Accounts'


class NotificationAdmin(admin.ModelAdmin):
    model = Notification
    list_display = ('name', 'text', 'notify_date', 'receiver')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return True


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'avatar')
    list_filter = ('is_active',)
    actions = [block_user, unblock_user]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        return True


accounts_site = AccountAdminArea(name='AccountAdmin')
accounts_site.register(CustomUser, CustomUserAdmin)
accounts_site.register(Notification, NotificationAdmin)
