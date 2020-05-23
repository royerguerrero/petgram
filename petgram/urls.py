"""petgram URL Configuration"""
# Django
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls, name='admin'),
    path('', include(('posts.urls', 'posts'), namespace='posts')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
