# Generated by Django 3.0.1 on 2020-07-26 21:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("game", "0004_gamepost_play"),
    ]

    operations = [
        migrations.AddField(
            model_name="gamepostcomment",
            name="dislikes",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="gamepostcomment",
            name="likes",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="gamepostcomment",
            name="views",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="gamepostimageurl",
            name="dislikes",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="gamepostimageurl",
            name="likes",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="gamepostimageurl",
            name="timestamp",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="gamepostimageurl",
            name="views",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
