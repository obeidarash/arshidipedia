# Generated by Django 4.0 on 2022-02-23 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0016_employer_national_code_alter_employer_lastname_fa'),
        ('accounting', '0022_remove_pay_payer'),
    ]

    operations = [
        migrations.AddField(
            model_name='pay',
            name='payer',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='office.employer', verbose_name='پرداخت کننده'),
        ),
        migrations.AlterField(
            model_name='fund',
            name='user',
            field=models.ForeignKey(default=False, help_text='کارمندی را انتخاب کنید که در شرکت شریک است', on_delete=django.db.models.deletion.CASCADE, to='office.employer', verbose_name='شریک'),
        ),
        migrations.AlterField(
            model_name='salary',
            name='to',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='office.employer', verbose_name='به حساب کارمند'),
        ),
    ]
