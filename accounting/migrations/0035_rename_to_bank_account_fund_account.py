# Generated by Django 4.0 on 2022-02-25 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0034_alter_fund_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fund',
            old_name='to_bank_account',
            new_name='account',
        ),
    ]
