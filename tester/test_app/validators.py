from django.core.exceptions import ValidationError
from django.db import models
from test_app.errors import CORRECT_ANSWER_NUMBER_ERROR


def validate_correct_answer_num(question, is_correct):
    from test_app.models import QuestionAnswer

    questions_with_true_count = (
        QuestionAnswer.objects.filter(question=question)
        .values("question")
        .annotate(
            true_count=models.Count(
                "is_correct", filter=models.F("is_correct")
            ),
            all_count=models.Count("is_correct"),
        )
    )

    true_answers_count = questions_with_true_count[0]["true_count"]
    if is_correct:
        true_answers_count += 1
    else:
        true_answers_count -= 1
    all_answers_count = questions_with_true_count[0]["all_count"]

    if not (1 <= true_answers_count < all_answers_count):
        raise ValidationError(CORRECT_ANSWER_NUMBER_ERROR)
