# Generated by Django 4.0 on 2022-03-04 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0024_invoiceitem_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.DateTimeField(verbose_name='تاریخ'),
        ),
    ]