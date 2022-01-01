# Generated by Django 4.0 on 2022-01-01 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0009_alter_contact_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='mobile_1',
            field=models.IntegerField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='mobile_2',
            field=models.BigIntegerField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='telephone',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]