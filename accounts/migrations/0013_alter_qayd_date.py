# Generated by Django 4.2.3 on 2024-05-03 11:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_remove_qayd_details_alter_qayd_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qayd',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 5, 3, 11, 52, 7, 982211, tzinfo=datetime.timezone.utc), null=True, verbose_name='تاريخ القيد'),
        ),
    ]
