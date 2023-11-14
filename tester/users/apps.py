from typing import Any

from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"

    def __init__(self, app_name: str, app_module: Any | None) -> None:
        super().__init__(app_name, app_module)
