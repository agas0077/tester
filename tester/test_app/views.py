from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView
from test_app.models import Test
from test_app.services import (chech_user_complete_test, delete_result,
                               delete_unfinished_test_results, get_all_results,
                               get_question_answers_context,
                               get_unanswered_questions_context,
                               mark_test_complete, save_user_result_form)


# Create your views here.
class IndexView(ListView):
    model = Test
    template_name = "index.html"

    def get(
        self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> HttpResponse:
        delete_unfinished_test_results(request.user)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        tests = Test.objects.all().values("pk")

        context["results"] = {}
        for test in tests:
            test_pk = test.get("pk")
            context["results"][test_pk] = get_all_results(
                self.request.user, test_pk=test_pk
            )
        return context


@require_http_methods(["GET", "POST"])
def take_test(request, test_pk):
    template_name = "question_form.html"

    if chech_user_complete_test(request.user, test_pk):
        delete_result(request.user, test_pk)

    if request.method == "POST":
        save_user_result_form(request, test_pk)

    question_params = {
        "user": request.user,
        "test_pk": test_pk,
    }
    context = get_unanswered_questions_context(**question_params)

    if context.get("next_question_pk") is None:
        mark_test_complete(request.user, test_pk=test_pk)
        return redirect("test-app:index")

    context = get_question_answers_context(context["question"], context)

    return render(request, template_name, context)
