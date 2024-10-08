from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User
from basicinfo.models import LegalPersons, TypePayment, TypeDelivery, TypeTransaction, Cities, States, Region, Countries
from companys.models import Company
from employees.models import Employee
from products.models import Items

class Customers(models.Model):
    companyID = models.ForeignKey(Company, on_delete=models.PROTECT, blank=True)
    sequence = models.PositiveIntegerField(editable=False)  # الحقل التسلسلي
    legalPersonID = models.OneToOneField(LegalPersons, on_delete=models.CASCADE, blank=True)
    def __str__(self):
        return  str(self.legalPersonID) + ' : ID : ' + str(self.sequence)

class Inventory (models.Model):
    companyID = models.ForeignKey(Company, on_delete=models.PROTECT,blank=True)
    sequence = models.PositiveIntegerField(editable=False)  # الحقل التسلسلي
    name_ar = models.CharField(verbose_name='المخزن عربي', max_length=100)
    name_en = models.CharField(verbose_name='المخزن إنجليزي', max_length=100, blank=True, null=True)
    countryID = models.ForeignKey(Countries, verbose_name='الدولة', default=1, on_delete=models.PROTECT, blank=True, null=True) 
    regionID = models.ForeignKey(Region, verbose_name='المنطقة', default=1, on_delete=models.PROTECT, blank=True, null=True)
    stateID = models.ForeignKey(States, verbose_name='الولاية', default=1, on_delete=models.PROTECT, blank=True, null=True)
    cityID = models.ForeignKey(Cities, verbose_name='المدينة', default=1, on_delete=models.PROTECT, blank=True, null=True) 
    address = models.CharField(verbose_name='وصف العنوان', max_length=100, blank=True, null=True)
    google_maps_location = models.URLField(verbose_name='العنوان على خرائط قوقل', max_length=500, blank=True, null=True)
    administrator = models.ForeignKey(Employee, verbose_name='الموظف المسؤول', on_delete=models.PROTECT, blank=True, null=True)
    phoneAdmin = models.CharField(verbose_name='هاتف الموظف المسؤول', max_length=100, blank=True, null=True)
    def __str__(self):
        return str(self.name_ar)

class InvoicesSalesHead (models.Model):
    companyID = models.ForeignKey(Company, on_delete=models.CASCADE,blank=True)
    sequence = models.PositiveIntegerField(editable=False)  # الحقل التسلسلي
    date = models.DateField(verbose_name='التاريخ', blank=True, null=True)
    typeTransactionID = models.ForeignKey(TypeTransaction, verbose_name='نوع العملية', default=4, on_delete=models.PROTECT, blank=True, null=True)
    inventoryID = models.ForeignKey(Inventory, verbose_name='المخزن', on_delete=models.PROTECT, blank=True, null=True)
    customerID = models.ForeignKey(Customers, verbose_name='العميل', related_name='sales_customer', on_delete=models.PROTECT)
    currencyID = models.ForeignKey(Countries , verbose_name='العملة', default=3, on_delete=models.PROTECT, blank=True, null=True)
    rate = models.DecimalField(verbose_name='سعر الصرف', default=1, max_digits=6, decimal_places=2, blank=True, null=True)
    typePaymentID = models.ForeignKey(TypePayment, verbose_name='طريقة الدفع', default=1, on_delete=models.PROTECT, blank=True, null=True)
    typeDeliveryID = models.ForeignKey(TypeDelivery, verbose_name='طريقة التسليم', default=1, on_delete=models.PROTECT, blank=True, null=True)
    description = models.TextField(verbose_name='الوصف', default="مبيعات", max_length=250, blank=True, null=True)
    recipient = models.CharField(verbose_name='المستلم',max_length=100, blank=True, null=True)
    address = models.CharField(verbose_name='عنوان المستلم',max_length=200, blank=True, null=True)
    google_maps_location = models.URLField(verbose_name='العنوان على خرائط قوقل', max_length=500, blank=True, null=True)
    phone = models.CharField(verbose_name='رقم هاتف المستلم',max_length=50, blank=True, null=True)
    phoneOther = models.CharField(verbose_name='هاتف آخر',max_length=50, blank=True, null=True)
    details = models.ManyToManyField(Items, through='InvoicesSalesBody', related_name='invoices', blank=True)
    salesRepID = models.ForeignKey(Employee, verbose_name='مندوب المبيعات', on_delete=models.PROTECT, blank=True, null=True)
    attachments = models.FileField(verbose_name='المرفقات',upload_to='attach_sales', blank=True, null=True)
    approve = models.BooleanField(verbose_name='إعتماد', default=False, blank=True, null=True) 
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='created_by_invoS', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='تاريخ الإنشاء',auto_now_add=True, blank=True, null=True)
    updated_by = models.ForeignKey(User, verbose_name='المُعدِل', related_name='updated_by_invoS', on_delete=models.PROTECT, blank=True, null=True)
    updated_at = models.DateTimeField(verbose_name='تاريخ التعديل', auto_now=True, blank=True, null=True)
  
    def __str__(self):
        return f"Invoice {self.id} - {self.customerID}"
    
    @property
    def total_price_after_tax(self):
        """حساب إجمالي السعر بعد الضريبة من تفاصيل الفاتورة."""
        return self.sales_invoice.aggregate(total=Sum('total_price_after_tax'))['total'] or 0
  
class InvoicesSalesBody(models.Model):
    invoiceHeadID = models.ForeignKey(InvoicesSalesHead, on_delete=models.DO_NOTHING, related_name='sales_invoice', blank=True)
    itemID = models.ForeignKey(Items, verbose_name='المنتج', on_delete=models.PROTECT,related_name='sales_details', blank=True, null=True)
    inventoryID = models.ForeignKey(Inventory, verbose_name='المخزن', on_delete=models.PROTECT, blank=True, null=True)
    quantity = models.DecimalField(verbose_name='الكمية', default=1, max_digits=6, decimal_places=0, blank=True, null=True)
    unit_price = models.DecimalField(verbose_name='سعر البيع', default=1, max_digits=10, decimal_places=2, blank=True, null=True)
    discount = models.DecimalField(verbose_name='خصم مسموح به', default=0, max_digits=6, decimal_places=2, blank=True, null=True)
    total_price_before_tax = models.DecimalField(verbose_name='السعر قبل الضريبة', max_digits=10, decimal_places=2, blank=True, null=True)
    tax_rate = models.DecimalField(verbose_name='نسبة الضريبة', default=0, max_digits=6, decimal_places=2, blank=True, null=True)
    tax_value = models.DecimalField(verbose_name='قيمة الضريبة', default=0, max_digits=6, decimal_places=2, blank=True, null=True)
    total_price_after_tax = models.DecimalField(verbose_name='إجمالي السعر بعد الضريبة', max_digits=10, decimal_places=2, blank=True, null=True)
    total_price_local_currency = models.DecimalField(verbose_name='إجمالي السعر عملة محلية ', max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.total_price_before_tax =  (self.unit_price - self.discount) * self.quantity
        self.tax_value = self.total_price_before_tax * self.tax_rate / 100
        self.total_price_after_tax = self.total_price_before_tax + self.tax_value
        self.total_price_local_currency = self.total_price_after_tax / self.invoiceHeadID.rate
        super().save(*args, **kwargs)

    @property
    def total_items(self):
        return self.itemID.count()
    
    def __str__(self):
        return f"{self.itemID} - {self.quantity} x {self.unit_price} = {self.total_price_after_tax}"
