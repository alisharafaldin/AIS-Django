# Generated by Django 4.2.3 on 2024-09-07 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companys', '0003_company_includeindalilalaemal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='includeInDalilAlaemal',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='تضمين في دليل الأعمال'),
        ),
    ]
