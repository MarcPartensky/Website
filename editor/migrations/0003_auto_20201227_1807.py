# Generated by Django 3.0.1 on 2020-12-27 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("editor", "0002_auto_20201227_1705"),
    ]

    operations = [
        migrations.AlterField(
            model_name="script",
            name="read",
            field=models.DateTimeField(auto_now=True),
        ),
    ]