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
    # Django Admin
    path('admin/', admin.site.urls, name='admin'),
    # Posts
    path('', posts_views.feed, name='posts'),
    path('posts/new/', posts_views.new_post, name='new_post'),
    # Users
    path('users/login/', users_views.login_view, name='login'),
    path('users/logout/', users_views.logout_view, name='logout'),
    path('users/singup/', users_views.singup_view, name='singup'),
    path('users/me/profile/', users_views.update_profile, name='update_profile'),
    # Others
    path('hi/<str:name>/<int:age>/', local_views.hi, name='hi'),
    path('sort-numbers/', local_views.sorted_numbers, name='sort'),
    path('hello-world/', local_views.hello_world, name='hello'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
