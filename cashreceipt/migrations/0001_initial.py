# Generated by Django 4.2.3 on 2024-09-15 06:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companys', '0007_alter_company_legalpersonid'),
        ('sales', '0023_invoicessalesbody_inventoryid_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employees', '0002_rename_employeeinfo_employee'),
        ('accounts', '0007_qayd_invoicessalesid_alter_qayd_typetransactionid'),
        ('basicinfo', '0025_alter_basicinfo_attachments'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashReceiptHead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.PositiveIntegerField(editable=False)),
                ('date', models.DateField(blank=True, null=True, verbose_name='التاريخ')),
                ('amountCredit', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='المبلغ الدائن')),
                ('rate', models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=6, null=True, verbose_name='سعر الصرف')),
                ('amountDebit_local_currency', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='المبلغ الدائع عملة محلية ')),
                ('description', models.TextField(blank=True, default='سند قبض', max_length=250, null=True, verbose_name='الوصف')),
                ('attachments', models.FileField(blank=True, null=True, upload_to='attach_cashreceipt', verbose_name='المرفقات')),
                ('approve', models.BooleanField(blank=True, default=False, null=True, verbose_name='إعتماد')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاريخ الإنشاء')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='تاريخ التعديل')),
                ('accountID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.accountstree', verbose_name='الحساب الدائن')),
                ('companyID', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='companys.company')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='created_by_cashreceipt', to=settings.AUTH_USER_MODEL)),
                ('currencyID', models.ForeignKey(blank=True, default=3, null=True, on_delete=django.db.models.deletion.PROTECT, to='basicinfo.countries', verbose_name='العملة')),
                ('customerID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cashreceipt', to='sales.customers', verbose_name='العميل')),
                ('employeeID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='employees.employee', verbose_name='الموظف')),
                ('typePaymentID', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='basicinfo.typepayment', verbose_name='طريقة الدفع')),
                ('typeTransactionID', models.ForeignKey(blank=True, default=2, null=True, on_delete=django.db.models.deletion.PROTECT, to='basicinfo.typetransaction', verbose_name='نوع العملية')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updated_by_cashreceipt', to=settings.AUTH_USER_MODEL, verbose_name='المُعدِل')),
            ],
        ),
        migrations.CreateModel(
            name='ReceiptAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allocated_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='المبلغ المخصص')),
                ('cashReceiptID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='allocations', to='cashreceipt.cashreceipthead', verbose_name='سند القبض')),
                ('salesInvoicesID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='allocated_receipts', to='sales.invoicessalesbody', verbose_name='فاتورة المبيعات')),
            ],
        ),
        migrations.CreateModel(
            name='CashReceiptBody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amountDebit', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='المبلغ المدين')),
                ('rate', models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=6, null=True, verbose_name='سعر الصرف')),
                ('transactionNumber', models.TextField(blank=True, max_length=50, null=True, verbose_name='رقم العملية')),
                ('description', models.TextField(blank=True, default='سند قبض', max_length=250, null=True, verbose_name='الوصف')),
                ('amountDebit_local_currency', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='المبلغ المدين عملة محلية ')),
                ('accountID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.accountstree', verbose_name='الحساب المدين')),
                ('cashReceiptHeadID', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='cash_receipt', to='cashreceipt.cashreceipthead')),
                ('currencyID', models.ForeignKey(blank=True, default=3, null=True, on_delete=django.db.models.deletion.PROTECT, to='basicinfo.countries', verbose_name='العملة')),
            ],
        ),
    ]