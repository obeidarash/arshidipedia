# Generated by Django 4.0 on 2022-02-01 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0003_letter_content_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letter',
            name='content',
        ),
    ]