# Generated by Django 4.2.13 on 2024-07-08 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0006_requests"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Requests",
            new_name="Request",
        ),
    ]
