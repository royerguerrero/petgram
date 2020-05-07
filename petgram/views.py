"""Petgram views"""
# Django
from django.http import HttpResponse, JsonResponse

# Utilities
from datetime import datetime

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Oh, hi! Current server time is {now}')

def sorted_numbers(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    numbers.sort()
    data = {
        'status': 'Ok', 
        'sorted numbers': numbers,
        'message': 'Numbers sorted successfully.' 
    }

    return JsonResponse(data)

def hi(request, name, age):
    if age <= 12:
        message = f'😥Sorry {name.capitalize()}, you are not allowed here'
    else:
        message = f'👋Hello {name.capitalize()}, welcome to my website'

    return HttpResponse(message)

