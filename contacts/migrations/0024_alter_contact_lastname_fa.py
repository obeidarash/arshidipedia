# Generated by Django 4.0 on 2022-02-24 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0023_alter_contact_hashtag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='lastname_fa',
            field=models.CharField(max_length=64, verbose_name='نام خانوادگی به فارسی'),
        ),
    ]