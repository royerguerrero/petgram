"""Users views"""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Exceptions 
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Profile

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

@login_required
def logout_view(request):
    """Logout view"""
    logout(request)
    return redirect('login')
    

def singup_view(request):
    """Register user"""
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confiramtion']

        if password != password_confirmation:
            return render(request, 'users/register.html', {'error': 'Las contraseñas no coinciden'})

        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'users/register.html', {'error': 'El username ya esta en uso'})
            

        user.email = email
        user.save()

        profile = Profile.objects.create(user=user)

        return redirect('login')

    return render(request, 'users/register.html')