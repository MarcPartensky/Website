# Generated by Django 3.0.1 on 2021-01-27 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20210127_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='read',
            field=models.DateTimeField(null=True),
        ),
    ]
