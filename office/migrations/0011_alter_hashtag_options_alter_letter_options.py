# Generated by Django 4.0 on 2022-02-06 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0010_alter_hashtag_options_alter_letter_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hashtag',
            options={'verbose_name': 'برچسب', 'verbose_name_plural': 'برچسب'},
        ),
        migrations.AlterModelOptions(
            name='letter',
            options={'verbose_name': 'نامه', 'verbose_name_plural': 'نامه'},
        ),
    ]
