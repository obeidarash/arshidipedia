# Generated by Django 4.0 on 2022-02-01 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_company_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('slug', models.SlugField(max_length=128, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='hashtag',
            field=models.ManyToManyField(blank=True, null=True, to='contacts.Hashtag'),
        ),
        migrations.AddField(
            model_name='contact',
            name='hashtag',
            field=models.ManyToManyField(blank=True, null=True, to='contacts.Hashtag'),
        ),
    ]
