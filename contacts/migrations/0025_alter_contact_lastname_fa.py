# Generated by Django 4.0 on 2022-02-24 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0024_alter_contact_lastname_fa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='lastname_fa',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='نام خانوادگی به فارسی'),
        ),
    ]
