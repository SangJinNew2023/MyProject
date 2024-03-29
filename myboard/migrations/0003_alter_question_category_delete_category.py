# Generated by Django 4.1.6 on 2023-03-29 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myboard", "0002_alter_category_category_alter_question_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="category",
            field=models.CharField(
                choices=[
                    ("QnA", "QnA"),
                    ("Free", "Free"),
                    ("Python", "Python"),
                    ("Go", "Go"),
                    ("Javascript", "Javascript"),
                    ("Notice", "Notice"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.DeleteModel(
            name="Category",
        ),
    ]
