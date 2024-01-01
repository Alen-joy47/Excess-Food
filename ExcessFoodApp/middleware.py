# myapp/middleware.py
from django.shortcuts import redirect
from django.urls import reverse

class CheckSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request is not a login page and either 'userid' or 'donorid' is not present in the session
        if not request.path.startswith(reverse('index')) and ('userid' not in request.session and 'donorid' not in request.session):
            # Redirect to the login page or any other appropriate action
            return redirect(reverse('index'))  # Replace 'login_page' with your login page URL

        response = self.get_response(request)
        return response
