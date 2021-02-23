# Generated by Django 3.0.1 on 2021-02-13 20:08

from django.db import migrations, models
import shortuuidfield.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='written_count',
            new_name='write_count',
        ),
        migrations.AlterField(
            model_name='access',
            name='id',
            field=shortuuidfield.fields.ShortUUIDField(blank=True, default='67_sW1', editable=False, max_length=22, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='token',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]