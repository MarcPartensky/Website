# Generated by Django 3.0.1 on 2021-01-31 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0007_auto_20210127_0120"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="update_count",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
