"""Petgram middleware catalog"""

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
        pass
