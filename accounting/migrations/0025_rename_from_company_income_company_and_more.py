# Generated by Django 4.0 on 2022-02-23 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0024_alter_pay_source_alter_pay_to'),
    ]

    operations = [
        migrations.RenameField(
            model_name='income',
            old_name='from_company',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='income',
            old_name='from_contact',
            new_name='contact',
        ),
    ]
