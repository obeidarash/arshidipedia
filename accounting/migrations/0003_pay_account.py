# Generated by Django 4.0 on 2022-01-06 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0002_bankaccount_pay_comment_pay_date_of_payment_pay_fee_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pay',
            name='account',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='accounting.bankaccount'),
        ),
    ]
