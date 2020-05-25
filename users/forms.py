"""Users forms"""

# Django 
from django import forms
from django.forms import ModelForm

# Models 
from django.contrib.auth.models import User
from users.models import Profile

class SignupForm(forms.Form):
    """Sign up form."""
    username = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=150, required=True)
    password = forms.CharField(max_length=50, required=True)
    password_confirmation = forms.CharField(max_length=50, required=True)
    
    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')

        return data

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()

class ProfileForm(forms.Form):
    """Profile form"""

    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=10, required=True)

    website = forms.URLField(max_length=200, required=False)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=True)
    picture = forms.ImageField(required=False)
