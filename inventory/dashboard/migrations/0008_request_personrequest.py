# Generated by Django 4.2.13 on 2024-07-08 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0007_rename_requests_request"),
    ]

    operations = [
        migrations.AddField(
            model_name="request",
            name="personRequest",
            field=models.CharField(max_length=30, null=True),
        ),
    ]
