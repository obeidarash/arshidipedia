# Generated by Django 4.0 on 2022-02-01 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0009_alter_company_hashtag_alter_contact_hashtag'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='type',
            field=models.CharField(blank=True, choices=[('private', 'Private Address'), ('invoice', 'Invoice Address'), ('delivery ', 'Delivery Address'), ('other', 'Other Address')], default=('delivery ', 'Delivery Address'), max_length=128),
        ),
    ]
