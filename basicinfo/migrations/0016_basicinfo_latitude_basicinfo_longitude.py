# Generated by Django 4.2.3 on 2024-09-08 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicinfo', '0015_alter_basicinfo_countryid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicinfo',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='خط العرض'),
        ),
        migrations.AddField(
            model_name='basicinfo',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='خط الطول'),
        ),
    ]
