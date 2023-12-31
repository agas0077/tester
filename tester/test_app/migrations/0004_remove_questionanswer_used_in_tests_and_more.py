# Generated by Django 4.2.7 on 2023-11-13 11:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("test_app", "0003_alter_questionanswer_used_in_tests"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="questionanswer",
            name="used_in_tests",
        ),
        migrations.AddField(
            model_name="question",
            name="used_in_tests",
            field=models.ManyToManyField(
                blank=True,
                related_name="questions",
                to="test_app.test",
                verbose_name="Used in tests",
            ),
        ),
    ]
