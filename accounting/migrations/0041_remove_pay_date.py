# Generated by Django 4.0 on 2022-01-18 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0040_pay_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pay',
            name='date',
        ),
    ]
