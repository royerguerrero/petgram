"""Views posts"""
# Django
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Utilities
from datetime import datetime

# Models
from posts.models import Post

# Forms
from posts.forms import PostForm

posts = [
    {
		'title': 'Mont Blanc',
		'user': {
			'name': 'Yésica Cortés',
			'picture': 'https://picsum.photos/60/60/?image=1027'
		},
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'photo': 'https://picsum.photos/800/600?image=1036',
	},
	{
		'title': 'Via Láctea',
		'user': {
			'name': 'Christian Van der Henst',
			'picture': 'https://picsum.photos/60/60/?image=1005'
		},
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'photo': 'https://picsum.photos/800/800/?image=903',
	},
	{
		'title': 'Nuevo auditorio',
		'user': {
			'name': 'Uriel (thespianartist)',
			'picture': 'https://picsum.photos/60/60/?image=883'
		},
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'photo': 'https://picsum.photos/500/700/?image=1076',
	}
]

@login_required
def feed(request):
    """Return a posts"""
    posts = Post.objects.all().order_by('-created')
    return render(request, 'posts/feed.html', {'posts': posts})

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
			return redirect('posts')
		
	else:
		form = PostForm()

	return render(request, 'posts/new.html', {'form': form})
