# Generated by Django 4.0 on 2022-01-06 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0011_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='account_number',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='card_number',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='shaba',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
