# Generated by Django 3.0.1 on 2020-07-26 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20200726_2130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gamepostcomment',
            old_name='game',
            new_name='gamepost',
        ),
    ]