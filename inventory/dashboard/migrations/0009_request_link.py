# Generated by Django 4.2.13 on 2024-07-08 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0008_request_personrequest"),
    ]

    operations = [
        migrations.AddField(
            model_name="request",
            name="link",
            field=models.URLField(null=True),
        ),
    ]
