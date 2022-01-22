# Generated by Django 4.0 on 2022-01-14 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0037_pay_taxation_currency'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='salary',
            options={'verbose_name_plural': 'Salaries'},
        ),
        migrations.AddField(
            model_name='salary',
            name='price_currency',
            field=models.CharField(blank=True, choices=[('IRR', 'Rial'), ('USD', 'US Dollar')], default=('IRR', 'Rial'), max_length=32),
        ),
        migrations.AlterField(
            model_name='pay',
            name='source',
            field=models.CharField(choices=[('employer', 'Employer'), ('company', 'Company')], default=('employer', 'Employer'), help_text='it means you spend money form your pocket or the company', max_length=32),
        ),
    ]