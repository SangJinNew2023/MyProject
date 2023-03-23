# Generated by Django 4.1.6 on 2023-03-23 12:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myinventory_users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                default="default.jpg",
                upload_to="Profile_images",
                validators=[
                    django.core.validators.FileExtensionValidator(["png", "jpg"])
                ],
            ),
        ),
    ]
