"""Posts models"""
# Django
from django.db import models 
# Models
from django.contrib.auth.models import User
from users.models import Profile

class Post(models.Model):
    """Post Model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.Case)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} by @{self.user.username}'

