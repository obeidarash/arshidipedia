# Generated by Django 4.0 on 2022-01-06 16:13

from django.db import migrations, models
import django.utils.timezone
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0013_pay_taxation_pay_taxation_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='pay',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pay',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='pay',
            name='taxation',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=0, default_currency='IRR', help_text='Taxation and VAT', max_digits=14, null=True),
        ),
    ]
