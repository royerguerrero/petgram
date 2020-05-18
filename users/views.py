"""Users views"""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    """Login view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('posts')
        else:
            return render(request, 'users/login.html', {'error': 'El usuario o contraseña son invalidos', 'user': '132'})

    return render(request, 'users/login.html')
    