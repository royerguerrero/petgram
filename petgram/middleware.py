"""Petgram middleware catalog"""
# Django
from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    """ Profile completion middleware

    Ensure every user that is intecating with the plataform
    have their profile picture and biography
    """

    def __init__(self, get_response):
        """middleware initianilation"""
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        """Code to be excluted for each request before the view is called"""
        if not request.user.is_anonymous and not request.user.is_staff:
            profile = request.user.profile
            if not profile.picture or not profile.biography:
                allowed_urls = [
                    reverse('update_profile'),
                    reverse('logout'),
                    reverse('admin:index')
                ]
                if request.path not in allowed_urls:
                    return redirect('update_profile')

        response = self.get_response(request)
        return response
