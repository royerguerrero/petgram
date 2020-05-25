"""Users views"""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView, FormView, UpdateView

# Exceptions 
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Profile
from posts.models import Post

# Forms 
from users.forms import ProfileForm, SignupForm

class UserDetailView(LoginRequiredMixin, DetailView):
    """User ditail view"""
    template_name = "users/detail.html"
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context

def login_view(request):
    """Login view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('posts:posts')
        else:
            return render(request, 'users/login.html', {'error': 'El usuario o contraseña son invalidos', 'user': '132'})

    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    """Logout view"""
    logout(request)
    return redirect('users:login')
    

class SignupView(FormView):
    """Regiter user"""
    template_name = 'users/register.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data"""
        form.save()
        return super().form_valid(form)

@login_required
def update_profile(request):
    """Update a user's profile view."""
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile = request.user.profile
            user = request.user

            user.first_name = data['first_name']
            user.last_name = data['last_name']

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            # Ckecks that the picture is not empty when the form is reloaded
            if data['picture']:
                profile.picture = data['picture']

            user.save()
            profile.save()

            return redirect('posts:posts')
    
    else:
        form = ProfileForm()

    return render(request, 'users/update_profile.html', {'form': form})