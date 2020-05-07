"""petgram URL Configuration"""
# Django
from django.urls import path
# Local
from petgram import views

urlpatterns = [
    path('hi/<str:name>/<int:age>/', views.hi),
    path('sort-numbers/', views.sorted_numbers),
    path('hello-world/', views.hello_world),
]
