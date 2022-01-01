# Generated by Django 4.0 on 2022-01-01 16:50

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0012_contact_address_contact_city_contact_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='country',
            field=django_countries.fields.CountryField(default='IR', max_length=2),
        ),
    ]