import csv
import datetime as dt
import pathlib

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from test_app.models import Answer, Question, QuestionAnswer, Test

User = get_user_model()


class Command(BaseCommand):
    """Пакетная загрузка данных в базу"""

    def handle(self, *args, **kwargs):
        try:
            print(self.load_tests())
        except Exception as error:
            raise Exception(f"Error on loading {error}")

    def load_tests(self):
        file_to_load = pathlib.Path(settings.BASE_DIR, "test_data", "data.csv")
        with file_to_load.open(encoding="utf-8") as r_file:
            file_reader = csv.reader(r_file, delimiter=";")
            count = 0
            QuestionAnswer.objects.all().delete()
            Answer.objects.all().delete()
            Question.objects.all().delete()
            Test.objects.all().delete()
            for row in file_reader:
                if count == 0:
                    print(f'Data contains columns: {", ".join(row)}')
                else:
                    test_name = row[0]
                    test_description = row[1]
                    question = row[2]
                    answer_option = row[3]
                    answer_correct_flag = True if row[4] == "TRUE" else "False"

                    # Get or crerate a test
                    test, _ = Test.objects.get_or_create(
                        name=test_name, description=test_description
                    )

                    # Get or create a question object
                    question, _ = Question.objects.get_or_create(
                        question=question
                    )
                    question.used_in_tests.add(test)

                    # Create answer object
                    answer, _ = Answer.objects.get_or_create(
                        answer=answer_option
                    )

                    # Get or create question-answer obejct add it to the relevant
                    # test
                    QuestionAnswer.objects.get_or_create(
                        question=question,
                        answer=answer,
                        is_correct=answer_correct_flag,
                    )

                count += 1

        return f"Tests are loaded - {count} rows"
