"""petgram URL Configuration"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('👋Hello world!')

urlpatterns = [
    path('hello', hello_world)
]
