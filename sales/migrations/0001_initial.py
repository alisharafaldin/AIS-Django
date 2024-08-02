# Generated by Django 4.2.3 on 2024-08-02 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0008_itemdetails_targetgroupid_and_more'),
        ('basicinfo', '0016_deliverymethod'),
        ('companys', '0009_alter_company_businesstypeid_delete_businesstype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.PositiveIntegerField(editable=False)),
                ('companyID', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='companys.company')),
                ('legalPersonsID', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='basicinfo.legalpersons')),
            ],
        ),
        migrations.CreateModel(
            name='SalesInvoiceHead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.PositiveIntegerField(editable=False)),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='التاريخ')),
                ('description', models.TextField(blank=True, default='فاتورة مبيعات جديدة', max_length=250, null=True, verbose_name='الوصف')),
                ('attachments', models.FileField(blank=True, null=True, upload_to='', verbose_name='المرفقات')),
                ('approve', models.BooleanField(blank=True, default=False, null=True, verbose_name='إعتماد')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاريخ الإنشاء')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='تاريخ التعديل')),
                ('companyID', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='companys.company')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='created_by_invoS', to=settings.AUTH_USER_MODEL)),
                ('supplierID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.customers', verbose_name='العميل')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updated_by_invoS', to=settings.AUTH_USER_MODEL, verbose_name='المُعدِل')),
            ],
        ),
        migrations.CreateModel(
            name='SalesInvoiceBody',
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
                ('salesinvoiceHeadID', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='salesinvoice_details', to='sales.salesinvoicehead')),
            ],
        ),
    ]
