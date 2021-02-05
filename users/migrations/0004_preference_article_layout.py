# Generated by Django 3.0.1 on 2021-02-05 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210115_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='preference',
            name='article_layout',
            field=models.CharField(choices=[('bootstrap3', 'Bootstrap3'), ('github', 'Github'), ('jasonm23-dark', 'Jasonm23 Dark'), ('jasonm23-foghorn', 'Jasonm23 Foghorn'), ('jasonm23-markdown', 'Jasonm23 Markdown'), ('jasonm23-swiss', 'Jasonm23 Swiss'), ('marc', 'Marc'), ('markedapp-byword', 'Markedapp Byword'), ('mixu-book', 'Mixu Book'), ('mixu_bootstrap-2col', 'Mixu Bootstrap 2Col'), ('mixu-bootstrap', 'Mixu Bootstrap'), ('mixu-gray', 'Mixu Gray'), ('mixu-page', 'Mixu Page'), ('mixu-radar', 'Mixu Radar'), ('roryg_ghostwriter', 'Roryg Ghostwriter'), ('thomasf_solarizedcssdark', 'Thomasf Solarizedcssdark'), ('thomasf_solarizedcsslight', 'Thomasf Solarizedcsslight')], max_length=255, null=True),
        ),
    ]
