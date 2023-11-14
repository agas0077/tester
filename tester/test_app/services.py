from deepdiff import DeepDiff
from django.db.models import Count, Q
from test_app.forms import UserResultForm
from test_app.models import Answer, Question, QuestionAnswer, UserResult


def get_unanswered_questions_context(
    user,
    test_pk,
):
    context = dict()
    filters = [
        Q(used_in_tests__pk=test_pk),
        ~Q(user_results__user=user),
    ]

    unanswered_questions = Question.objects.filter(*filters)

    num = len(unanswered_questions)

    if num >= 1:
        question = unanswered_questions.first()
        context["question"] = question
        next_question_pk = unanswered_questions.last().pk
        context["next_question_pk"] = next_question_pk

    return context


def get_question_answers_context(question_obj, context={}):
    answers = Answer.objects.filter(
        question_answer_answer__question=question_obj
    )
    context["answers"] = answers
    return context


def save_user_result_form(request, test_pk):
    form_data = request.POST.copy()
    form_data["user"] = request.user
    form_data["test"] = test_pk

    answers = [value for key, value in form_data.items() if "answer" in key]

    forms = []
    is_correct = check_correct_answer(form_data["question"], answers)
    for answer in answers:
        form_data["answer"] = answer
        form_data["result"] = is_correct
        form = UserResultForm(form_data)
        if form.is_valid():
            forms.append(form)
        else:
            return form

    for form in forms:
        form.save()


def check_correct_answer(question_pk, answers):
    correct_answers = QuestionAnswer.objects.filter(
        question=question_pk, answer__in=answers, is_correct=True
    ).count()
    return len(answers) == correct_answers


def get_all_results(user, test_pk):
    user_result = (
        UserResult.objects.filter(user=user, test=test_pk, result=True)
        .values("test")
        .annotate(score=Count("question", distinct=True))
        .values("score")
    )
    try:
        user_result = user_result[0]["score"]
    except IndexError:
        user_result = 0
    questions_n = Question.objects.filter(used_in_tests=test_pk).count()
    percentage = round(user_result / questions_n, 2) * 100
    return {
        "user_result": user_result,
        "questions_n": questions_n,
        "percentage": f"{percentage}%",
    }


def delete_result(user, test_pk):
    UserResult.objects.filter(user=user, test=test_pk).delete()


def delete_unfinished_test_results(user):
    UserResult.objects.filter(user=user, test_complete=False).delete()


def mark_test_complete(user, test_pk):
    UserResult.objects.filter(user=user, test=test_pk).update(
        test_complete=True
    )


def chech_user_complete_test(user, test_pk):
    return UserResult.objects.filter(
        user=user, test=test_pk, test_complete=True
    ).exists()
