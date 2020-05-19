"""Users forms"""

# Django 
from django import forms

class ProfileForm(forms.Form):
    """Profile form"""

    website = forms.URLField(max_length=200, required=False)
    biography = forms.CharField(max_length=500, required=False)
    phone = forms.CharField(max_length=20, required=True)
