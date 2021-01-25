"""Views posts"""
# Django
from django.forms.widgets import SelectDateWidget
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, FormView

# Utilities
from datetime import datetime

from django.views.generic.edit import FormView

# Models
from posts.models import Post

# Forms
from posts.forms import PostForm


class PostFeedView(LoginRequiredMixin, ListView):
    """Return all published posts"""
    model = Post
    template_name = "posts/feed.html"
    ordering = ('-created',)
    paginate_by = 15
    context_object_name = "posts"


class PostDetailView(LoginRequiredMixin, DetailView):
    """Shows the detail of a post"""
    model = Post
    template_name = 'posts/detail.html'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, FormView):
    """Create a new post"""
    template_name = 'posts/new.html'
    form_class = PostForm
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.data._mutable = True
        form.data['user'] = request.user
        form.data['profile'] = request.user.profile
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('posts:posts')
    