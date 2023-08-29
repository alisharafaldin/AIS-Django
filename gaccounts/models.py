from django.db import models
from django.contrib.auth.models import User
from employees.models import EmpInfo
from basicinfo.models import Project, Currency
from hadena.models import ShareholdersInfo
# Create your models here.

class AccType(models.Model):
    accType_ar = models.CharField(verbose_name='نوع الحساب عربي',max_length=100, blank=True, null=True)
    accType_en = models.CharField(verbose_name='نوع الحساب نجليزي',max_length=100, blank=True, null=True)
    def __str__(self):
        return str(self.accType_ar)
    
class AccDorC(models.Model):
    accDorC_ar = models.CharField(verbose_name='طبيعة الحساب عربي',max_length=100, blank=True, null=True)
    accDorC_en = models.CharField(verbose_name='طبيعة الحساب نجليزي',max_length=100, blank=True, null=True)
    def __str__(self):
        return str(self.accDorC_ar)

class AccBudget(models.Model):
    accBudget_ar = models.CharField(verbose_name=' حساب الميزانية عربي',max_length=100, blank=True, null=True)
    accBudget_en = models.CharField(verbose_name=' حساب الميزانية نجليزي',max_length=100, blank=True, null=True)
    def __str__(self):
        return str(self.accBudget_ar)

class AccountsTree(models.Model):
    accName_ar = models.CharField(verbose_name='إسم الحساب عربي',max_length=100, blank=True, null=True)
    accName_en = models.CharField(verbose_name='إسم الحساب إنجليزي',max_length=100, blank=True, null=True)
    accTypeID = models.ForeignKey(AccType, verbose_name='نوع الحساب', on_delete=models.CASCADE)
    accBudgetID = models.ForeignKey(AccBudget , verbose_name='حساب الميزانية', on_delete=models.CASCADE)
    accDorCID = models.ForeignKey(AccDorC , verbose_name='طبيعة الحساب', on_delete=models.CASCADE)
    accParentID = models.CharField(verbose_name='الحساب الأب', max_length=100, blank=True, null=True)
    accCode = models.CharField(verbose_name='رمز الحساب',max_length=100, blank=True, null=True)
    accDes = models.CharField(verbose_name='رمز الحساب',max_length=100, blank=True, null=True)
    is_can_pay = models.BooleanField(verbose_name='إمكانية الدفع والتحصيل بهذا الحساب')
    def __str__(self):
        return str(self.accName_ar)

class Qayd(models.Model):
    userID = models.ForeignKey(User, verbose_name='المستخدم', on_delete=models.CASCADE, null=True)
    dateQayd = models.DateField(verbose_name='تاريخ القيد',)
    desQayd = models.TextField(verbose_name='وصف القيد', max_length=250, blank=True, null=True)
    currencyID = models.ForeignKey(Currency , verbose_name='العملة', default=1, on_delete=models.CASCADE, null=True)
    attachments = models.FileField(verbose_name='مرفقات القيد', blank=True, null=True)
    details = models.ManyToManyField(AccountsTree, through='QaydDetails')
    def __str__(self):
        # return ' | Qayd id: ' + str(self.id)
        return  str(self.id)

class QaydDetails(models.Model):
    qaydID = models.ForeignKey(Qayd, verbose_name='رأس القيد', default=1, on_delete=models.CASCADE)
    accID = models.ForeignKey(AccountsTree, verbose_name='الحساب', default=1,  on_delete=models.CASCADE, blank=True, null=True)
    debit = models.DecimalField(max_digits=6, verbose_name='مدين', decimal_places=2)
    credit = models.DecimalField(max_digits=6, verbose_name='دائن', decimal_places=2)
    desQaydDetails = models.TextField(verbose_name='وصف تصفيل القيد', max_length=250,blank=True, null=True)
    projectID = models.ForeignKey(Project, verbose_name='المشروع', default=1,  on_delete=models.CASCADE, blank=True, null=True)
    empID = models.ForeignKey(EmpInfo, verbose_name='الموظف', default=1,  on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        # return 
        return str(self.id)
    class Meta:
        #ترتيب العناصر حسب الآي دي
        ordering = ['-id']

class TypeBond(models.Model):
    typeBond_ar = models.CharField(verbose_name='نوع السند عربي',max_length=100)
    typeBond_en = models.CharField(verbose_name='نوع السند إنجليزي',max_length=100,blank=True, null=True)
    def __str__(self):
        return str(self.typeID_ar)
    
class BondsCatchPay(models.Model):
    userID = models.ForeignKey(User, verbose_name='أمين الصندوق', on_delete=models.CASCADE)
    typeBondID = models.ForeignKey(TypeBond, verbose_name='نوع السند',on_delete=models.CASCADE)
    dateBond = models.DateField(verbose_name='تاريخ السند',)
    currencyID = models.ForeignKey(Currency , verbose_name='العملة', on_delete=models.CASCADE)
    exchangeRate = models.DecimalField(verbose_name='سعر الصرف', max_digits=6, decimal_places=2)
    amount = models.DecimalField(verbose_name='المبلغ', max_digits=6, decimal_places=2)
    description = models.CharField(verbose_name='الوصف',max_length=100)
    recipient = models.CharField(verbose_name='المستلم',max_length=100, blank=True, null=True)
    empID = models.ForeignKey(EmpInfo, verbose_name='الموظف', on_delete=models.CASCADE, blank=True, null=True)
    shareholderID = models.ForeignKey(ShareholdersInfo, verbose_name='المساهم', on_delete=models.CASCADE, blank=True, null=True)
    projectID = models.ForeignKey(Project, verbose_name='المشروع', on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return str(self.typeBondID)
