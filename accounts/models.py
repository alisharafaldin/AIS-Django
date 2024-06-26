from django.db import models
from django.contrib.auth.models import User
from basicinfo.models import Project, Countries
# from hadena.models import ShareholdersInfo, Cycle
from employees.models import EmpInfo
from datetime import datetime
from django.utils import timezone
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

class AccountsTree(models.Model):
  name_ar = models.CharField(verbose_name='إسم الحساب عربي',max_length=100, blank=True, null=True)
  name_en = models.CharField(verbose_name='إسم الحساب إنجليزي',max_length=100, blank=True, null=True)
  typeID = models.ForeignKey(AccountType, verbose_name='نوع الحساب', default=1, on_delete=models.CASCADE)
  natureID = models.ForeignKey(AccountNature , verbose_name='طبيعة الحساب', default=1, on_delete=models.CASCADE)
  categoryID = models.ForeignKey(AccountCategory , verbose_name='تصنيف حساب ', default=1, on_delete=models.CASCADE)
  code = models.CharField(verbose_name='رمز الحساب',max_length=100, blank=True, null=True)
  description = models.CharField(verbose_name='وصف الحساب',max_length=100, blank=True, null=True)
  is_can_pay = models.BooleanField(verbose_name='إمكانية الدفع والتحصيل بهذا الحساب')
  def __str__(self):
    return str(self.name_ar)
    
class TypeTransaction(models.Model):
  typeTransaction_ar = models.CharField(verbose_name='نوع المعاملة عربي',max_length=100)
  typeTransaction_en = models.CharField(verbose_name='نوع المعاملة إنجليزي',max_length=100,blank=True, null=True)
  def __str__(self):
    return str(self.typeTransaction_ar)
    
class Qayd(models.Model):
  typeTransactionID = models.ForeignKey(TypeTransaction , verbose_name='نوع العملية', default=1, on_delete=models.CASCADE, null=True)
  date = models.DateField(verbose_name='تاريخ القيد', default=timezone.now() , blank=True, null=True)
  description = models.TextField(verbose_name='وصف القيد', max_length=250, blank=True, null=True)
  attachments = models.FileField(verbose_name='مرفقات القيد', blank=True, null=True)
  created_py = models.ForeignKey(User, verbose_name='المُنشئ', related_name='qayds', on_delete=models.CASCADE)
  created_dt = models.DateTimeField(verbose_name='تاريخ الإنشاء',auto_now_add=True)
  updated_py = models.ForeignKey(User, verbose_name='المُعدل', related_name='+', on_delete=models.CASCADE, blank=True, null=True)
  updated_dt = models.DateTimeField(verbose_name='تاريخ التعديل', blank=True, null=True)
  def __str__(self):
    # return ' | Qayd id: ' + str(self.id)
    return  str(self.id)

class QaydDetails(models.Model):
  qaydID = models.ForeignKey(Qayd, verbose_name='رأس القيد', default=1, on_delete=models.CASCADE)
  date_details = models.DateField(verbose_name='التاريخ', default=datetime.now(), blank=True, null=True)
  accountID = models.ForeignKey(AccountsTree, verbose_name='الحساب', default=1, on_delete=models.CASCADE, blank=True, null=True)
  currencyID = models.ForeignKey(Countries , verbose_name='العملة', default=1, on_delete=models.CASCADE, null=True)
  rate = models.DecimalField(max_digits=6, verbose_name='سعر الصرف', default=1, decimal_places=2)
  debit = models.DecimalField(max_digits=6, verbose_name='مدين', default=0, decimal_places=2)
  credit = models.DecimalField(max_digits=6, verbose_name='دائن', default=0, decimal_places=2)
  description_details = models.TextField(verbose_name='وصف تفصيل القيد', max_length=250,blank=True, null=True)
  projectID = models.ForeignKey(Project, verbose_name='المشروع', default=1, on_delete=models.CASCADE, blank=True, null=True)
  empID = models.ForeignKey(EmpInfo, verbose_name='الموظف',on_delete=models.CASCADE, blank=True, null=True)
  # shareholdersID = models.ForeignKey(ShareholdersInfo, related_name='المساهم', verbose_name='المساهم', default=1, on_delete=models.CASCADE, blank=True, null=True)
  # cycleID = models.ForeignKey(Cycle, related_name='cycleID', verbose_name='الدورة', default=1, on_delete=models.CASCADE, blank=True, null=True)
  def __str__(self):
    # return 
    return str(self.qaydID)
  class Meta:
    #ترتيب العناصر حسب الآي دي
    ordering = ['-id']
