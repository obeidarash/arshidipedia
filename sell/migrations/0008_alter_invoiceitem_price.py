# Generated by Django 4.0 on 2022-02-19 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0007_rename_satellite_product_invoiceitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceitem',
            name='price',
            field=models.BigIntegerField(verbose_name='مبلغ'),
        ),
    ]
