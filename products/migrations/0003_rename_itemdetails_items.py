# Generated by Django 4.2.3 on 2024-08-06 04:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_rename_itemsdetailsid_order_itemid_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companys', '0002_rename_legalpersonid_company_legalpersonid'),
        ('purchases', '0002_rename_itemsdetailstid_invoicebody_itemid_and_more'),
        ('sales', '0003_rename_legalpersonsid_customers_legalpersonid_and_more'),
        ('basicinfo', '0005_measuringunits_paymentmethods_and_more'),
        ('products', '0002_itemdetails_itemcode_itemdetails_measuringunitid'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ItemDetails',
            new_name='Items',
        ),
    ]