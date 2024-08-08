# Generated by Django 4.2.3 on 2024-08-06 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicinfo', '0005_measuringunits_paymentmethods_and_more'),
        ('sales', '0005_invoicessaleshead_deliverymethodid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoicessaleshead',
            name='typeTransactionID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='basicinfo.typetransaction', verbose_name='نوع العملية'),
            preserve_default=False,
        ),
    ]