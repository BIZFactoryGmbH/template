from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

from authn.apps.core.views import letsencrypt, index


urlpatterns = [
    path('', index, name='index'),
    path('.well-known/acme-challenge/pFmV21J6LJi3E4H0rY6iUDjSjVJmLlSGCnPs3u0Y', letsencrypt),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
path('api-auth/', obtain_auth_token),
    path('user/', include('authn.apps.user.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
