# Generated by Django 4.0 on 2022-02-04 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0018_alter_contact_hashtag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='hashtag',
            field=models.ManyToManyField(blank=True, null=True, to='contacts.Hashtag', verbose_name='برچسب'),
        ),
    ]