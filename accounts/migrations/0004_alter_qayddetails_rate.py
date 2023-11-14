# Generated by Django 4.2.3 on 2023-11-14 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_qayd_currencyid_qayddetails_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qayddetails',
            name='rate',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=6, verbose_name='سعر الصرف'),
        ),
    ]
