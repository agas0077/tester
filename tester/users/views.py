from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import CustomUserCreationForm

User = get_user_model()


class UserCreateView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("test-app:index")
    template_name = "signup.html"
