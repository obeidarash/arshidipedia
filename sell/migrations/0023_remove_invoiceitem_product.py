# Generated by Django 4.0 on 2022-02-25 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0022_invoiceitem_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoiceitem',
            name='product',
        ),
    ]