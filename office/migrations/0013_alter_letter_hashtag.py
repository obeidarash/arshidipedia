# Generated by Django 4.0 on 2022-02-10 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0012_alter_letter_hashtag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='hashtag',
            field=models.ManyToManyField(blank=True, to='office.Hashtag', verbose_name='برچسب'),
        ),
    ]
