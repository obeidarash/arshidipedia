# Generated by Django 4.0 on 2022-02-22 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0006_alter_invoice_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='is_cancel',
            field=models.BooleanField(default=False, verbose_name='لغو شده؟'),
        ),
    ]
