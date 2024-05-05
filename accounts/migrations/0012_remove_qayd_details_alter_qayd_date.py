# Generated by Django 4.2.3 on 2024-05-03 11:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_qayd_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qayd',
            name='details',
        ),
        migrations.AlterField(
            model_name='qayd',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 5, 3, 11, 46, 55, 292622, tzinfo=datetime.timezone.utc), null=True, verbose_name='تاريخ القيد'),
        ),
    ]
