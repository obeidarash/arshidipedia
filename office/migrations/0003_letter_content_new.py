# Generated by Django 4.0 on 2022-02-01 20:26

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0002_letter_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='content_new',
            field=tinymce.models.HTMLField(default=False),
            preserve_default=False,
        ),
    ]
