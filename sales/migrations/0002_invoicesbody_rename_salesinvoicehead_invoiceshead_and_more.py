# Generated by Django 4.2.3 on 2024-08-02 15:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_itemdetails_targetgroupid_and_more'),
        ('companys', '0009_alter_company_businesstypeid_delete_businesstype'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoicesBody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=6, null=True, verbose_name='الكمية')),
                ('unit_price', models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=10, null=True, verbose_name='سعر الشراء')),
                ('discount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True, verbose_name='خصم مكتسب')),
                ('total_price_before_tax', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='السعر قبل الضريبة')),
                ('tax_rate', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True, verbose_name='نسبة الضريبة')),
                ('tax_value', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True, verbose_name='قيمة الضريبة')),
                ('total_price_after_tax', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='إجمالي السعر بعد الخصم')),
                ('itemsDetailstID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.itemdetails', verbose_name='المنتج')),
            ],
        ),
        migrations.RenameModel(
            old_name='SalesInvoiceHead',
            new_name='InvoicesHead',
        ),
        migrations.DeleteModel(
            name='SalesInvoiceBody',
        ),
        migrations.AddField(
            model_name='invoicesbody',
            name='salesinvoiceHeadID',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='sales_invoice', to='sales.invoiceshead'),
        ),
    ]
