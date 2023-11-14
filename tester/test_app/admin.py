from django.contrib import admin
# Register your models here.
from test_app.models import Answer, Question, QuestionAnswer, Test, UserResult


class AnswerAdmin(admin.ModelAdmin):
    list_display = ["pk", "answer"]


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["pk", "question"]


class QuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ["pk", "question", "answer", "is_correct"]
    search_fields = [
        "question__question",
        "answer__answer",
        "is_correct",
    ]


class TestAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "description"]


class UserResultAdmin(admin.ModelAdmin):
    pass


admin.site.register(Answer, AnswerAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionAnswer, QuestionAnswerAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(UserResult, UserResultAdmin)
