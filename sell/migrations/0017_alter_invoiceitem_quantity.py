# Generated by Django 4.0 on 2022-02-25 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0016_alter_invoiceitem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceitem',
            name='quantity',
            field=models.BigIntegerField(verbose_name='مقدار'),
        ),
    ]
