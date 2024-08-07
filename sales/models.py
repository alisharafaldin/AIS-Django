from django.db import models
from django.contrib.auth.models import User
from basicinfo.models import LegalPersons, PaymentMethods, DeliveryMethods, MeasuringUnits, TypeTransaction
from companys.models import Company
from django.utils import timezone
from django.db.models.signals import pre_save, post_delete
from products.models import Items

class Customers(models.Model):
    companyID = models.ForeignKey(Company, on_delete=models.PROTECT, blank=True)
    sequence = models.PositiveIntegerField(editable=False)  # الحقل التسلسلي
    legalPersonID = models.OneToOneField(LegalPersons, on_delete=models.CASCADE, blank=True)
    def __str__(self):
        return  str(self.legalPersonID) 
  
class InvoicesSalesHead (models.Model):
    companyID = models.ForeignKey(Company, on_delete=models.PROTECT,blank=True)
    sequence = models.PositiveIntegerField(editable=False)  # الحقل التسلسلي
    customerID = models.ForeignKey(Customers, verbose_name='العميل', on_delete=models.PROTECT)
    paymentMethodID = models.ForeignKey(PaymentMethods, verbose_name='طريقة الدفع', on_delete=models.PROTECT, blank=True, null=True)
    deliveryMethodID = models.ForeignKey(DeliveryMethods, verbose_name='طريقة التسليم', on_delete=models.PROTECT, blank=True, null=True)
    typeTransactionID = models.ForeignKey(TypeTransaction, verbose_name='نوع العملية', on_delete=models.PROTECT, blank=True, null=True)
    date = models.DateTimeField(verbose_name='التاريخ', default=timezone.now , blank=True, null=True)
    description = models.TextField(verbose_name='الوصف', default="فاتورة مبيعات جديدة", max_length=250, blank=True, null=True)
    attachments = models.FileField(verbose_name='المرفقات', blank=True, null=True)
    approve = models.BooleanField(verbose_name='إعتماد', default=False, blank=True, null=True) 
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='created_by_invoS', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='تاريخ الإنشاء',auto_now_add=True, blank=True, null=True)
    updated_by = models.ForeignKey(User, verbose_name='المُعدِل', related_name='updated_by_invoS', on_delete=models.PROTECT, blank=True, null=True)
    updated_at = models.DateTimeField(verbose_name='تاريخ التعديل', auto_now=True, blank=True, null=True)
    
    def __str__(self):
        return f"Invoice {self.id} - {self.customerID}"
  
class InvoicesSalesBody(models.Model):
    invoiceHeadID = models.ForeignKey(InvoicesSalesHead, on_delete=models.CASCADE, related_name='sales_invoice', blank=True)
    itemID = models.ForeignKey(Items, verbose_name='المنتج', on_delete=models.PROTECT, blank=True, null=True)
    quantity = models.DecimalField(verbose_name='الكمية', default=1, max_digits=6, decimal_places=2, blank=True, null=True)
    measuringUnitID = models.ForeignKey(MeasuringUnits, verbose_name='وحدة القياس', on_delete=models.PROTECT, blank=True, null=True)
    unit_price = models.DecimalField(verbose_name='سعر البيع', default=1, max_digits=10, decimal_places=2, blank=True, null=True)
    discount = models.DecimalField(verbose_name='خصم مسموح به', default=0, max_digits=6, decimal_places=2, blank=True, null=True)
    total_price_before_tax = models.DecimalField(verbose_name='السعر قبل الضريبة', max_digits=10, decimal_places=2, blank=True, null=True)
    tax_rate = models.DecimalField(verbose_name='نسبة الضريبة', default=0, max_digits=6, decimal_places=2, blank=True, null=True)
    tax_value = models.DecimalField(verbose_name='قيمة الضريبة', default=0, max_digits=6, decimal_places=2, blank=True, null=True)
    total_price_after_tax = models.DecimalField(verbose_name='إجمالي السعر بعد الخصم', max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.total_price_before_tax =  (self.unit_price - self.discount) * self.quantity
        self.tax_value = self.total_price_before_tax * self.tax_rate / 100
        self.total_price_after_tax = self.total_price_before_tax + self.tax_value
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.itemsDetailstID} - {self.quantity} x {self.unit_price} = {self.total_price_after_tax}"
