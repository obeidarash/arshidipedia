# Generated by Django 4.0 on 2022-01-01 18:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0029_alter_company_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='website',
            field=models.URLField(blank=True, max_length=512, null=True, validators=[django.core.validators.URLValidator]),
        ),
    ]
