# Generated by Django 4.2.3 on 2023-11-14 13:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_accountstatement_accountcategory_statementid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qayd',
            name='currencyID',
        ),
        migrations.AddField(
            model_name='qayddetails',
            name='rate',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True, verbose_name='سعر الصرف'),
        ),
    ]
