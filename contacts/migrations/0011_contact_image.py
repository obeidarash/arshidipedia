# Generated by Django 4.0 on 2022-02-02 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0010_address_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='image',
            field=models.ImageField(default=False, height_field=200, upload_to='contact', width_field=200),
            preserve_default=False,
        ),
    ]