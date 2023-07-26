from django.shortcuts import redirect, resolve_url
from django.urls import reverse, reverse_lazy


class AuthenticationMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.path.startswith('/account/login/') or request.user.is_authenticated and request.path.startswith(
                '/account/register/'):
            return redirect(reverse_lazy('home page'))

        response = self.get_response(request)
        return response
