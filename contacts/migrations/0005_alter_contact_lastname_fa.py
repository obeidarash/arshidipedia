# Generated by Django 4.0 on 2022-01-01 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_contact_lastname_en_contact_name_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='lastname_fa',
            field=models.CharField(max_length=64),
        ),
    ]