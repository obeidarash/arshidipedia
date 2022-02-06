# Generated by Django 4.0 on 2022-02-04 15:26

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('contacts', '0017_alter_address_options_alter_company_options_and_more'),
        ('office', '0009_rename_content_new_letter_content_letter_number_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hashtag',
            options={'verbose_name': 'برچسب', 'verbose_name_plural': 'برچسب ها'},
        ),
        migrations.AlterModelOptions(
            name='letter',
            options={'verbose_name': 'نامه', 'verbose_name_plural': 'نامه ها'},
        ),
        migrations.AlterField(
            model_name='hashtag',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='hashtag',
            name='slug',
            field=models.SlugField(help_text='به انگلیسی و مختصر باشد به جای اسپیس از خط تیره استفاده شود', max_length=128, unique=True, verbose_name='اسلاگ'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='content',
            field=tinymce.models.HTMLField(verbose_name='متن نامه'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='date',
            field=models.DateField(verbose_name='تاریخ'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='hashtag',
            field=models.ManyToManyField(to='office.Hashtag', verbose_name='برچسب'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='number',
            field=models.CharField(max_length=64, verbose_name='شماره'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='send_with',
            field=models.CharField(blank=True, choices=[('email', 'ایمیل'), ('fax', 'فکس'), ('post', 'پست'), ('delivery', 'پیک'), ('employer', 'کارمند')], default=('delivery', 'پیک'), max_length=32, null=True, verbose_name='نحوه ارسال'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='subject',
            field=models.CharField(max_length=512, verbose_name='موضوع'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='to_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.company', verbose_name='به شرکت'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='to_contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.contact', verbose_name='به مخاطب'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='type',
            field=models.CharField(blank=True, choices=[('virtual', 'مجازی (پی دی اف)'), ('physical', 'فیزیکی')], default=('physical', 'فیزیکی'), max_length=32, null=True, verbose_name='نوع نامه'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='writer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='نویسنده'),
        ),
    ]