# Generated by Django 4.2.13 on 2024-07-08 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0009_request_link"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inventory",
            name="name",
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="name",
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name="request",
            name="name",
            field=models.CharField(max_length=300, null=True),
        ),
    ]
