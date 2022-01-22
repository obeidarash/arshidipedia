# Generated by Django 4.0 on 2022-01-06 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0016_received_bank_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='received',
            name='bank_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.bankaccount'),
        ),
    ]