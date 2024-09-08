# Generated by Django 4.2.3 on 2024-09-08 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicinfo', '0017_alter_basicinfo_latitude_alter_basicinfo_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicinfo',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=25, max_digits=30, null=True, verbose_name='خط العرض'),
        ),
        migrations.AlterField(
            model_name='basicinfo',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=25, max_digits=30, null=True, verbose_name='خط الطول'),
        ),
    ]