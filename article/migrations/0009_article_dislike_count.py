# Generated by Django 3.0.1 on 2021-02-01 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0008_article_update_count"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="dislike_count",
            field=models.PositiveIntegerField(default=0),
        ),
    ]