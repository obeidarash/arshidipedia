# Generated by Django 4.0 on 2022-02-23 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0016_employer_national_code_alter_employer_lastname_fa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='writer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='office.employer', verbose_name='نویسنده'),
        ),
    ]
