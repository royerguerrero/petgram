"""Users forms"""

# Django 
from django import forms

class ProfileForm(forms.Form):
    """Profile form"""

    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=10, required=True)

    website = forms.URLField(max_length=200, required=False)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=True)
    picture = forms.ImageField(required=False)
