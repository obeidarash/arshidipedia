# Generated by Django 4.0 on 2022-02-01 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0008_contact_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='hashtag',
            field=models.ManyToManyField(to='contacts.Hashtag'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='hashtag',
            field=models.ManyToManyField(to='contacts.Hashtag'),
        ),
    ]
