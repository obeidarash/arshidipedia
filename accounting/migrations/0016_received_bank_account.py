# Generated by Django 4.0 on 2022-01-06 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0015_alter_category_options_received'),
    ]

    operations = [
        migrations.AddField(
            model_name='received',
            name='bank_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting.bankaccount'),
        ),
    ]
