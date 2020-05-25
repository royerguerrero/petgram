"""Post urls"""

# Django 
from django.urls import path

# Views
from posts import views 

urlpatterns = [
    path('', views.PostFeedView.as_view(), name='posts'),
    path('posts/new/', views.PostCreateView.as_view(), name='new_post'),
    path('posts/<int:id>', views.PostDetailView.as_view(), name='detail_post'),
]
