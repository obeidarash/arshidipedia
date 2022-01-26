# Generated by Django 4.0 on 2022-01-25 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_alter_company_options'),
        ('accounting', '0042_alter_pay_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='officialinvoices',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.company'),
        ),
        migrations.AddField(
            model_name='officialinvoices',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.contact'),
        ),
    ]
