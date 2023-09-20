from django.db import models
from django.contrib.auth.models import User
from basicinfo.models import Project, Currency
from employees.models import EmpInfo
# from hadena.models import ShareholdersInfo
# Create your models here.

class AccountType(models.Model):
  type_ar = models.CharField(verbose_name='نوع الحساب عربي',max_length=100, blank=True, null=True)
  type_en = models.CharField(verbose_name='نوع الحساب نجليزي',max_length=100, blank=True, null=True)
  def __str__(self):
    return str(self.accType_ar)
    
class AccountNature(models.Model):
  nature_ar = models.CharField(verbose_name='طبيعة الحساب عربي',max_length=100, blank=True, null=True)
  nature_en = models.CharField(verbose_name='طبيعة الحساب نجليزي',max_length=100, blank=True, null=True)
  def __str__(self):
    return str(self.accDorC_ar)

class AccountBudget(models.Model):
  budget_ar = models.CharField(verbose_name=' حساب الميزانية عربي',max_length=100, blank=True, null=True)
  budget_en = models.CharField(verbose_name=' حساب الميزانية نجليزي',max_length=100, blank=True, null=True)
  def __str__(self):
    return str(self.accBudget_ar)

class AccountsTree(models.Model):
  name_ar = models.CharField(verbose_name='إسم الحساب عربي',max_length=100, blank=True, null=True)
  name_en = models.CharField(verbose_name='إسم الحساب إنجليزي',max_length=100, blank=True, null=True)
  typeID = models.ForeignKey(AccountType, verbose_name='نوع الحساب', on_delete=models.CASCADE)
  budgetID = models.ForeignKey(AccountBudget , verbose_name='حساب الميزانية', on_delete=models.CASCADE)
  dorCID = models.ForeignKey(AccountNature , verbose_name='طبيعة الحساب', on_delete=models.CASCADE)
  parentID = models.CharField(verbose_name='الحساب الأب', max_length=100, blank=True, null=True)
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
  userID = models.ForeignKey(User, verbose_name='المستخدم', on_delete=models.CASCADE, null=True)
  typeTransactionID = models.ForeignKey(TypeTransaction , verbose_name='نوع العملية', default=1, on_delete=models.CASCADE, null=True)
  date = models.DateField(verbose_name='تاريخ القيد',)
  description = models.TextField(verbose_name='وصف القيد', max_length=250, blank=True, null=True)
  currencyID = models.ForeignKey(Currency , verbose_name='العملة', default=1, on_delete=models.CASCADE, null=True)
  attachments = models.FileField(verbose_name='مرفقات القيد', blank=True, null=True)
  details = models.ManyToManyField(AccountsTree, through='QaydDetails')
  # shareholdersID = models.ForeignKey(ShareholdersInfo, verbose_name='المساهم', default=1, on_delete=models.CASCADE, blank=True, null=True)
  projectID = models.ForeignKey(Project, verbose_name='المشروع', default=1, on_delete=models.CASCADE, blank=True, null=True)
  # cycleID = models.ForeignKey(Cycle,related_name='cycleID', verbose_name='الدورة', default=1, on_delete=models.CASCADE, blank=True, null=True)
  empID = models.ForeignKey(EmpInfo, verbose_name='الموظف', default=1, on_delete=models.CASCADE, blank=True, null=True)
  def __str__(self):
    # return ' | Qayd id: ' + str(self.id)
    return  str(self.id)

class QaydDetails(models.Model):
  qaydID = models.ForeignKey(Qayd, verbose_name='رأس القيد', default=1, on_delete=models.CASCADE)
  accID = models.ForeignKey(AccountsTree, verbose_name='الحساب', default=1, on_delete=models.CASCADE, blank=True, null=True)
  date = models.DateField(verbose_name='التاريخ', blank=True, null=True)
  debit = models.DecimalField(max_digits=6, verbose_name='مدين', decimal_places=2)
  credit = models.DecimalField(max_digits=6, verbose_name='دائن', decimal_places=2)
  description = models.TextField(verbose_name='وصف تفصيل القيد', max_length=250,blank=True, null=True)
  # shareholdersID = models.ForeignKey(ShareholdersInfo, verbose_name='المساهم', default=1, on_delete=models.CASCADE, blank=True, null=True)
  projectID = models.ForeignKey(Project, verbose_name='المشروع', default=1, on_delete=models.CASCADE, blank=True, null=True)
  # cycleID = models.ForeignKey(Cycle,related_name='cycleID', verbose_name='الدورة', default=1, on_delete=models.CASCADE, blank=True, null=True)
  empID = models.ForeignKey(EmpInfo, verbose_name='الموظف', default=1, on_delete=models.CASCADE, blank=True, null=True)
  def __str__(self):
    # return 
    return str(self.id)
  class Meta:
    #ترتيب العناصر حسب الآي دي
    ordering = ['-id']
    
# class Bond(models.Model):
#   userID = models.ForeignKey(User, verbose_name='المستخدم', on_delete=models.CASCADE, null=True)
#   date = models.DateField(verbose_name='تاريخ السند',)
#   typeID = models.ForeignKey(TypeBond , verbose_name='نوع السند', default=1, on_delete=models.CASCADE, null=True)
#   description = models.TextField(verbose_name='وصف السند', max_length=250, blank=True, null=True)
#   attachment = models.FileField(verbose_name='مرفقات السند', blank=True, null=True)
#   def __str__(self):
#     # return ' | Qayd id: ' + str(self.id)
#     return  str(self.id)
  
# class BondDetails(models.Model):
#   bondID = models.ForeignKey(Bond, verbose_name='رأس السند', on_delete=models.CASCADE)
#   date = models.DateField(verbose_name='تاريخ السند',)
#   currencyID = models.ForeignKey(Currency , verbose_name='العملة', on_delete=models.CASCADE)
#   exchangeRate = models.DecimalField(verbose_name='سعر الصرف', max_digits=6, decimal_places=2)
#   amount = models.DecimalField(verbose_name='المبلغ', max_digits=6, decimal_places=2)
#   description = models.CharField(verbose_name='الوصف',max_length=100)
#   recipient = models.CharField(verbose_name='المستلم',max_length=100, blank=True, null=True)
#   empID = models.ForeignKey(EmpInfo, verbose_name='الموظف', on_delete=models.CASCADE, blank=True, null=True)
#   # shareholderID = models.ForeignKey(ShareholdersInfo, verbose_name='المساهم', on_delete=models.CASCADE, blank=True, null=True)
#   projectID = models.ForeignKey(Project, verbose_name='المشروع', on_delete=models.CASCADE, blank=True, null=True)
#   def __str__(self):
#     return str(self.typeBondID)
