# Generated by Django 4.0 on 2022-01-11 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0018_alter_pay_fee_currency_alter_pay_price_currency_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficialInvoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True)),
                ('employer_signature', models.BooleanField(default=False)),
                ('location', models.CharField(choices=[('company_office', 'Company Office'), ('employer_office', 'Employer Office')], default=('company_office', 'Company Office'), max_length=64)),
                ('status', models.CharField(choices=[('current', 'Current'), ('invalid', 'Invalid'), ('lost', 'Lost')], default=('current', 'Current'), max_length=64)),
                ('serial_number', models.CharField(max_length=32)),
                ('date_of_invoice', models.DateField()),
                ('comment', models.TextField(blank=True, null=True)),
            ],
        ),
    ]