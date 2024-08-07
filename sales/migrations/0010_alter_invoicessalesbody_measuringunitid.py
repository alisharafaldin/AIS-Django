# Generated by Django 4.2.3 on 2024-08-07 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicinfo', '0005_measuringunits_paymentmethods_and_more'),
        ('sales', '0009_rename_supplierid_invoicessaleshead_customerid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicessalesbody',
            name='measuringUnitID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='basicinfo.measuringunits', verbose_name='وحدة القياس'),
        ),
    ]
