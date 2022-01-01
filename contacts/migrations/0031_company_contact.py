# Generated by Django 4.0 on 2022-01-01 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0030_contact_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.contact'),
        ),
    ]
