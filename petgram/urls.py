"""petgram URL Configuration"""
# Django
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
# Local
from petgram import views as local_views
from posts import views as posts_views
from users import views as users_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', posts_views.list_posts, name='posts'),
    path('hi/<str:name>/<int:age>/', local_views.hi, name='hi'),
    path('sort-numbers/', local_views.sorted_numbers, name='sort'),
    path('hello-world/', local_views.hello_world, name='hello'),
    path('users/login', users_views.login_view, name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
