# Third Party Library
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse_lazy


class LoginRequiredMiddleware:
    """
    Проверяет авторизован ли пользователь.
    При необходимости, перенаправляет его на страницу входа.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.login_url = settings.LOGIN_URL
        self.open_urls = [reverse_lazy(self.login_url)] + getattr(
            settings, "OPEN_URLS", []
        )

    def __call__(self, request):
        if (
            not request.user.is_authenticated
            and request.path_info not in self.open_urls
        ):
            return redirect(self.login_url)

        return self.get_response(request)
