from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from users.accounts import accounts_site


urlpatterns = [
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('notifications.urls')),
    path('ams/', accounts_site.urls),  # accounts admin site
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
