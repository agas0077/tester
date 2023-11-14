from django import forms
from test_app.models import UserResult


class UserResultForm(forms.ModelForm):
    class Meta:
        model = UserResult
        fields = ["question", "answer", "test", "user", "result"]
