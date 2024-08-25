from django.db import models
from django.contrib.auth.models import User
from basicinfo.models import Project, Countries, TypeTransaction
from employees.models import Employee
from companys.models import Company
from django.utils import timezone
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.db.models.signals import post_save
from mptt.models import MPTTModel, TreeForeignKey
# from .models import AccountsTree
#  لتجنب مشكلة الاستيراد الدائري (Circular Import)
def get_shareholdersInfo():
      from hadena.models import ShareholdersInfo
      return ShareholdersInfo
def get_cycle():
      from hadena.models import Cycle
      return Cycle

# Create your models here.

class AccountType(models.Model):
  type_ar = models.CharField(verbose_name='نوع الحساب عربي',max_length=100, blank=True, null=True)
  type_en = models.CharField(verbose_name='نوع الحساب نجليزي',max_length=100, blank=True, null=True)
  def __str__(self):
    return str(self.type_ar)
    
class AccountNature(models.Model):
  nature_ar = models.CharField(verbose_name='طبيعة الحساب عربي',max_length=100, blank=True, null=True)
  nature_en = models.CharField(verbose_name='طبيعة الحساب نجليزي',max_length=100, blank=True, null=True)
  def __str__(self):
    return str(self.nature_ar)

class AccountStatement(models.Model):
  statement_ar = models.CharField(verbose_name='القائمة عربي',max_length=100, blank=True, null=True)
  statement_en = models.CharField(verbose_name='القائمة نجليزي',max_length=100, blank=True, null=True)
  def __str__(self):
    return str(self.statement_ar)

class AccountCategory(models.Model):
  statementID = models.ForeignKey(AccountStatement, verbose_name='القائمة', default=1, on_delete=models.CASCADE)
  category_ar = models.CharField(verbose_name=' تصنيف الحساب عربي',max_length=100, blank=True, null=True)
  category_en = models.CharField(verbose_name=' تصنيف الحساب نجليزي',max_length=100, blank=True, null=True)
  def __str__(self):
    return str(self.category_ar)

class AccountsTree(MPTTModel):
  companyID = models.ForeignKey(Company, on_delete=models.PROTECT,blank=True, null=True)
  name_ar = models.CharField(verbose_name='إسم الحساب عربي',max_length=100, blank=True, null=True)
  name_en = models.CharField(verbose_name='إسم الحساب إنجليزي',max_length=100, blank=True, null=True)
  typeID = models.ForeignKey(AccountType, verbose_name='نوع الحساب', default=1, on_delete=models.CASCADE, blank=True, null=True)
  natureID = models.ForeignKey(AccountNature , verbose_name='طبيعة الحساب', default=1, on_delete=models.CASCADE, blank=True, null=True)
  categoryID = models.ForeignKey(AccountCategory , verbose_name='تصنيف حساب ', default=1, on_delete=models.CASCADE, blank=True, null=True)
  code = models.CharField(verbose_name='رمز الحساب',max_length=100, blank=True, null=True)
  description = models.CharField(verbose_name='وصف الحساب',max_length=100, blank=True, null=True)
  is_can_pay = models.BooleanField(verbose_name='إمكانية الدفع', blank=True, null=True)
  is_can_pay = models.BooleanField(verbose_name='إمكانية الدفع', blank=True, null=True)
  parent = TreeForeignKey('self', verbose_name='الحساب الأب', on_delete=models.CASCADE, related_name='children', blank=True, null=True,)
  level = models.IntegerField(verbose_name='مستوى الحساب', blank=True, null=True)  # المستوى سيتم تحديده تلقائيًا

  class MPTTMeta:
    order_insertion_by = ['name_ar']
    
  def save(self, *args, **kwargs):
    # تحديد المستوى بناءً على وجود حساب أب أو عدمه
    if self.parent:
        self.level = self.parent.level + 1
    else:
        self.level = 1
    super().save(*args, **kwargs)

  def __str__(self):
    if self.companyID:
      return f"{self.name_ar} - {self.code} {self.companyID.legalPersonID.acronym_ar}"
    return f"{self.name_ar} - {self.code}"
    
class Qayd(models.Model):
  companyID = models.ForeignKey(Company, on_delete=models.PROTECT,blank=True)
  sequence = models.PositiveIntegerField(editable=False)  # الحقل التسلسلي
  typeTransactionID = models.ForeignKey(TypeTransaction , verbose_name='نوع العملية', default=1, on_delete=models.PROTECT, null=True)
  date = models.DateTimeField(verbose_name='التاريخ', default=timezone.now , blank=True, null=True)
  description = models.TextField(verbose_name='وصف القيد', default="قيد يومية جديد", max_length=250, blank=True, null=True)
  attachments = models.FileField(verbose_name='مرفقات القيد', blank=True, null=True)
  details = models.ManyToManyField(AccountsTree, through='QaydDetails', related_name='qayds', blank=True)
  posted = models.BooleanField(verbose_name='ترحيل', default=False, blank=True, null=True) 
  created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='qayds_created', blank=True, null=True)
  created_at = models.DateTimeField(verbose_name='تاريخ الإنشاء',auto_now_add=True, blank=True, null=True)
  updated_by = models.ForeignKey(User, verbose_name='المُعدِل', related_name='updated_qayds', on_delete=models.PROTECT, blank=True, null=True)
  updated_at = models.DateTimeField(verbose_name='تاريخ التعديل', auto_now=True, blank=True, null=True)
  def __str__(self):
    # return ' | Qayd id: ' + str(self.id)
    return  str(self.id)
  
  class Meta:
    #ترتيب العناصر حسب الآي دي
    ordering = ['sequence']

  def get_details_count(self):
        return QaydDetails.objects.filter(qaydID=self).count()
  
class QaydDetails(models.Model):
  qaydID = models.ForeignKey(Qayd, on_delete=models.CASCADE, related_name='qayd_details', blank=True)
  date_details = models.DateTimeField(verbose_name='التاريخ', default=timezone.now, blank=True, null=True)
  accountID = models.ForeignKey(AccountsTree, verbose_name='الحساب', default=1, on_delete=models.PROTECT, blank=True, null=True)
  currencyID = models.ForeignKey(Countries , verbose_name='العملة', default=1, on_delete=models.PROTECT, blank=True, null=True)
  rate = models.DecimalField(verbose_name='سعر الصرف', default=1, max_digits=6, decimal_places=2, blank=True, null=True)
  quantity = models.DecimalField(max_digits=6, verbose_name='الكمية', default=1, decimal_places=2, blank=True, null=True)
  debit = models.DecimalField(verbose_name='مدين', default=0, max_digits=6, decimal_places=2)
  credit = models.DecimalField(verbose_name='دائن', default=0, max_digits=6, decimal_places=2)
  description_details = models.TextField(verbose_name='وصف تفصيل القيد', default="تفاصيل قيد يومية جديد", max_length=250,blank=True, null=True)
  projectID = models.ForeignKey(Project, verbose_name='المشروع', on_delete=models.PROTECT, blank=True, null=True)
  empID = models.ForeignKey(Employee, verbose_name='الموظف', on_delete=models.PROTECT, blank=True, null=True)
  shareholdersID = models.ForeignKey(get_shareholdersInfo(), related_name='المساهم', verbose_name='المساهم', on_delete=models.PROTECT, blank=True, null=True)
  cycleID = models.ForeignKey(get_cycle(), related_name='cycleID', verbose_name='الدورة', on_delete=models.PROTECT, blank=True, null=True)

  def __str__(self):
    return str(self.qaydID)
  

  def get_currency_ar(self):
      return self.currencyID.get_currency_ar()

  # @property
  # def total_debit(self):
  #     return self.rate * self.debit * self.quantity 