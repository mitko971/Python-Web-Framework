from django.shortcuts import redirect
from django.urls import reverse_lazy


class AuthenticationAdminMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_staff and request.path.startswith('/admin'):
            return redirect(reverse_lazy('home page'))

        response = self.get_response(request)
        return response
