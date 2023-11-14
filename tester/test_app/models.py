from asyncio import constants
from collections.abc import Iterable
from email.policy import default

from django.contrib.auth import get_user_model
from django.db import models
from test_app.validators import validate_correct_answer_num

User = get_user_model()

USER_NAME = "User"
ANSWER_IS_CORRECT_NAME = "Is the answer correct?"

TEST_NAME_NAME = "Test name"
TESTS_DESCRIPTION_NAME = "Description"

QUESTION_QUESTIONS_NAME = "Question"
QUESTION_TEST_NAME = "Used in tests"

ANSWER_ANSWER_NAME = "Answer"

USER_RESULT_TEST_NAME = "Tests taken"
USER_RESULT_QUESTION_NAME = "Question taken"
USER_RESULT_ANSWER_NAME = "Answer given"
USER_RESULT_COMPLETE_NAME = "Is test complete?"

USER_TEST_CORRECT_ANSWERS_NAME = "Correct answers"


# Create your models here.
class Question(models.Model):
    question = models.TextField(QUESTION_QUESTIONS_NAME)
    used_in_tests = models.ManyToManyField(
        "Test",
        related_name="questions",
        verbose_name=QUESTION_TEST_NAME,
        blank=True,
    )

    def __str__(self) -> str:
        return self.question


class Answer(models.Model):
    answer = models.CharField(ANSWER_ANSWER_NAME, max_length=200)

    def __str__(self) -> str:
        return self.answer


class QuestionAnswer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.PROTECT,
        related_name="question_answer_question",
        verbose_name=QUESTION_QUESTIONS_NAME,
    )
    answer = models.ForeignKey(
        Answer,
        on_delete=models.PROTECT,
        related_name="question_answer_answer",
        verbose_name=ANSWER_ANSWER_NAME,
    )
    is_correct = models.BooleanField(ANSWER_IS_CORRECT_NAME)

    def clean(self):
        validate_correct_answer_num(self.question, self.is_correct)
        return super().clean()


class Test(models.Model):
    name = models.CharField(TEST_NAME_NAME, max_length=200)
    description = models.TextField(TESTS_DESCRIPTION_NAME)

    def __str__(self) -> str:
        return self.name


class UserResult(models.Model):
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        related_name="user_results",
        verbose_name=USER_RESULT_TEST_NAME,
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="user_results",
        verbose_name=USER_RESULT_QUESTION_NAME,
    )
    answer = models.ForeignKey(
        Answer,
        on_delete=models.CASCADE,
        related_name="user_results",
        verbose_name=USER_RESULT_ANSWER_NAME,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_results",
        verbose_name=USER_NAME,
    )
    test_complete = models.BooleanField(
        USER_RESULT_COMPLETE_NAME, default=False
    )
    result = models.BooleanField(ANSWER_IS_CORRECT_NAME, default=False)
