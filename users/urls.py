"""Users urls"""
# Django
from django.urls import path

# Views
from users import views

urlpatterns = [
    # Managment
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('singup/', views.SignupView.as_view(), name='singup'),
    path('me/profile/', views.update_profile, name='update_profile'),
    # Posts
    path('<str:username>', views.UserDetailView.as_view(template_name='users/detail.html'), name='detail'),
]
