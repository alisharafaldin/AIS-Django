# Generated by Django 4.2.3 on 2024-08-06 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicinfo', '0005_measuringunits_paymentmethods_and_more'),
        ('sales', '0006_invoicessaleshead_typetransactionid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoicessaleshead',
            name='measuringUnitID',
        ),
        migrations.AddField(
            model_name='invoicessalesbody',
            name='measuringUnitID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='basicinfo.measuringunits', verbose_name='وحدة القياس'),
            preserve_default=False,
        ),
    ]
