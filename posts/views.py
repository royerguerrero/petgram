"""Views posts"""
# Django
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

# Utilities
from datetime import datetime

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

class PostCreateView(LoginRequiredMixin, CreateView):
    """Create a new post"""

    model = Post
    template_name = 'posts/new.html'
    # form_class = PostForm
    fields = ['title', 'photo']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.profile = self.request.user.profile
        form.save()
        return super(PostCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('posts:posts')
    