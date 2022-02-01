# Generated by Django 4.0 on 2022-02-01 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0004_remove_letter_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letter',
            name='hashtag',
        ),
        migrations.AddField(
            model_name='letter',
            name='hashtag',
            field=models.ManyToManyField(blank=True, null=True, to='office.Hashtag'),
        ),
    ]
