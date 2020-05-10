"""petgram URL Configuration"""
# Django
from django.urls import path
# Local
from petgram import views as local_views
from posts import views as posts_views

urlpatterns = [
    path('hi/<str:name>/<int:age>/', local_views.hi),
    path('sort-numbers/', local_views.sorted_numbers),
    path('hello-world/', local_views.hello_world),
    path('posts/', posts_views.list_posts)
]
