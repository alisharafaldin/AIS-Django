# Generated by Django 4.2.3 on 2024-09-07 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companys', '0004_alter_company_includeindalilalaemal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='includeInDalilAlaemal',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='تضمين في دليل الأعمال'),
        ),
        migrations.AlterField(
            model_name='company',
            name='includeInInAccountingRecords',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='تضمين في السجلات المحاسبية'),
        ),
    ]
