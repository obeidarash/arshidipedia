# Generated by Django 4.0 on 2022-01-05 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0009_alter_pay_date_of_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pay',
            name='date_of_payment',
            field=models.DateField(),
        ),
    ]
