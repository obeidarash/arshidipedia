# Generated by Django 4.0 on 2022-02-04 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0010_delete_sell'),
    ]

    operations = [
        migrations.AddField(
            model_name='pay',
            name='attach',
            field=models.FileField(blank=True, null=True, upload_to='pay'),
        ),
    ]
