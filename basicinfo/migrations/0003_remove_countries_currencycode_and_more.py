# Generated by Django 4.2.3 on 2023-09-24 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicinfo', '0002_rename_countryname_ar_countries_name_ar_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countries',
            name='currencyCode',
        ),
        migrations.AddField(
            model_name='countries',
            name='fractional_ar',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='الكسر عربي'),
        ),
        migrations.AddField(
            model_name='countries',
            name='fractional_en',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='الكسر إنجليزي'),
        ),
        migrations.AddField(
            model_name='countries',
            name='symbol_ar',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='الرمز عربي'),
        ),
        migrations.AddField(
            model_name='countries',
            name='symbol_en',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='الرمز إنجليزي'),
        ),
    ]