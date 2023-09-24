# Generated by Django 4.2.3 on 2023-09-24 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicinfo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='countries',
            old_name='countryName_ar',
            new_name='name_ar',
        ),
        migrations.RenameField(
            model_name='countries',
            old_name='countryName_en',
            new_name='name_en',
        ),
        migrations.RemoveField(
            model_name='countries',
            name='nationality',
        ),
        migrations.AddField(
            model_name='countries',
            name='currencyCode',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='كود العملة'),
        ),
        migrations.AddField(
            model_name='countries',
            name='currency_ar',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='العملة عربي'),
        ),
        migrations.AddField(
            model_name='countries',
            name='currency_en',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='العملة إنجليزي'),
        ),
        migrations.AddField(
            model_name='countries',
            name='nationality_ar',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='الجنسية عربي'),
        ),
        migrations.AddField(
            model_name='countries',
            name='nationality_en',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='الجنسية إنجليزي'),
        ),
    ]
