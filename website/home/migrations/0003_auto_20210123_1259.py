# Generated by Django 3.0.1 on 2021-01-23 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_auto_20210123_1258"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notifiedmaillist",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
