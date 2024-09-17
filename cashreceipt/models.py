from django.db import models
from django.contrib.auth.models import User
from basicinfo.models import  TypePayment, TypeTransaction, Countries
from companys.models import Company
from employees.models import Employee
from accounts. models import AccountsTree
from sales.models import Customers, InvoicesSalesBody
# Create your models here.


class CashReceiptHead (models.Model):
    companyID = models.ForeignKey(Company, on_delete=models.PROTECT,blank=True)
    sequence = models.PositiveIntegerField(editable=False)  # الحقل التسلسلي
    date = models.DateField(verbose_name='التاريخ', blank=True, null=True)
    typeTransactionID = models.ForeignKey(TypeTransaction, verbose_name='نوع العملية', default=2, on_delete=models.PROTECT, blank=True, null=True)
    typePaymentID = models.ForeignKey(TypePayment, verbose_name='طريقة الدفع', default=1, on_delete=models.PROTECT, blank=True, null=True)
    accountID = models.ForeignKey(AccountsTree, verbose_name='الحساب الدائن', on_delete=models.PROTECT, blank=True, null=True)
    customerID = models.ForeignKey(Customers, verbose_name='العميل', related_name='cashreceipt', on_delete=models.PROTECT, blank=True, null=True)
    employeeID = models.ForeignKey(Employee, verbose_name='الموظف', on_delete=models.PROTECT, blank=True, null=True)
    amountCredit = models.DecimalField(verbose_name='المبلغ الدائن', default=0, max_digits=6, decimal_places=2)
    currencyID = models.ForeignKey(Countries , verbose_name='العملة', default=3, on_delete=models.PROTECT, blank=True, null=True)
    rate = models.DecimalField(verbose_name='سعر الصرف', default=1, max_digits=6, decimal_places=2, blank=True, null=True)
    amountDebit_local_currency = models.DecimalField(verbose_name='المبلغ الدائع عملة محلية ', max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(verbose_name='الوصف', default="سند قبض", max_length=250, blank=True, null=True)
    attachments = models.FileField(verbose_name='المرفقات',upload_to='attach_cashreceipt', blank=True, null=True)
    approve = models.BooleanField(verbose_name='إعتماد', default=False, blank=True, null=True) 
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='created_by_cashreceipt', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='تاريخ الإنشاء',auto_now_add=True, blank=True, null=True)
    updated_by = models.ForeignKey(User, verbose_name='المُعدِل', related_name='updated_by_cashreceipt', on_delete=models.PROTECT, blank=True, null=True)
    updated_at = models.DateTimeField(verbose_name='تاريخ التعديل', auto_now=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.amountDebit_local_currency = self.amountCredit / self.rate 
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{TypeTransaction.name_ar} رقم {self.id} - {self.customerID}"
  
class CashReceiptBody(models.Model):
    cashReceiptHeadID = models.ForeignKey(CashReceiptHead, on_delete=models.CASCADE, related_name='cash_receipt', blank=True)
    accountID = models.ForeignKey(AccountsTree, verbose_name='الحساب المدين', on_delete=models.PROTECT, blank=True, null=True)
    amountDebit = models.DecimalField(verbose_name='المبلغ المدين', default=0, max_digits=6, decimal_places=2)
    currencyID = models.ForeignKey(Countries , verbose_name='العملة', default=3, on_delete=models.PROTECT, blank=True, null=True)
    rate = models.DecimalField(verbose_name='سعر الصرف', default=1, max_digits=6, decimal_places=2, blank=True, null=True)
    transactionNumber = models.TextField(verbose_name='رقم العملية', max_length=50, blank=True, null=True)
    description = models.TextField(verbose_name='الوصف', default="سند قبض", max_length=250, blank=True, null=True)
    amountDebit_local_currency = models.DecimalField(verbose_name='المبلغ المدين عملة محلية ', max_digits=10, decimal_places=2, blank=True, null=True)
  
    def save(self, *args, **kwargs):
        self.amountDebit_local_currency = self.amountDebit / self.rate 
        super().save(*args, **kwargs)

    @property
    def total_row(self):
        return self.id.count()
    
    def __str__(self):
        return f" المبلغ المدين {self.accountID} العملة {self.currencyID} : {self.amountDebit} / {self.rate} = {self.amountDebit_local_currency}"

class ReceiptAllocation(models.Model):
    cashReceiptID = models.ForeignKey(CashReceiptHead, verbose_name='سند القبض', on_delete=models.CASCADE, related_name="allocations", blank=True, null=True)
    salesInvoicesID = models.ForeignKey(InvoicesSalesBody, verbose_name='فاتورة المبيعات', on_delete=models.CASCADE, related_name="allocated_receipts", blank=True, null=True)
    allocated_amount = models.DecimalField(verbose_name='المبلغ المخصص', max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Allocation of {self.allocated_amount} to Invoice #{self.salesInvoicesID.id}" 