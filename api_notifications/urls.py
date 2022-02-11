from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.i18n import JavaScriptCatalog
from django.urls import path, include

from users.accounts import accounts_site


urlpatterns = [
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('notifications.urls')),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catalog'),
    path('accounts/', accounts_site.urls),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
