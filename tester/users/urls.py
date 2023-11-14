from django.contrib.auth import views
from django.urls import path
from users.views import UserCreateView

app_name = "users"

urlpatterns = [
    path(
        "login/",
        views.LoginView.as_view(template_name="login.html"),
        name="login",
    ),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("signup/", UserCreateView.as_view(), name="signup"),
]
