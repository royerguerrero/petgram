"""Views posts"""
# Django
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

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
	paginate_by = 2
	context_object_name = "posts"

class PostDetailView(LoginRequiredMixin, DetailView):
	"""Shows the detail of a post"""
	model = Post
	template_name = 'posts/detail.html'
	slug_field = 'id'
	slug_url_kwarg = 'id'
	context_object_name = 'post'

@login_required
def new_post(request):
	"""Create a new post view"""
	if request.method == 'POST':
		request.POST = request.POST.copy()
		request.POST['user'] = request.user.pk
		request.POST['profile'] = request.user.profile.pk
		form = PostForm(request.POST, request.FILES)
		print(form.is_valid())
		if form.is_valid():
			form.save()
			return redirect('posts:posts')
		
	else:
		form = PostForm()

	return render(request, 'posts/new.html', {'form': form})
