# Generated by Django 4.2.3 on 2024-01-07 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicinfo', '0002_legalpersonality_created_dt_person_created_dt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='created_dt',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاريخ الإنشاء'),
        ),
    ]