# Generated by Django 4.0 on 2022-02-21 18:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0014_invoice_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceitem',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
