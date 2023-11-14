from django.urls import path
from test_app.views import IndexView, take_test

app_name = "test-app"


urlpatterns = [
    path("<int:test_pk>/", take_test, name="test"),
    path("<int:test_pk>/<int:question_pk>/", take_test, name="question"),
    path("", IndexView.as_view(), name="index"),
]
