
from django.db import models
from datetime import date 
from employees.models import EmpInfo
from basicinfo.models import Countries, Region, States, Cities, Person
from accounts.models import Qayd

class Cycle(models.Model):
  cycle_ar = models.CharField(verbose_name='الدورة عربي',max_length=100)
  cycle_er = models.CharField(verbose_name='الدورة إنجليزي',max_length=100, blank=True, null=True)
  directSupervisor = models.CharField(verbose_name='المشرف المباشر',max_length=100, blank=True, null=True)
  phoneDirectSupervisor = models.CharField(verbose_name='جوال المشرف المباشر',max_length=100, blank=True, null=True)
  countryID = models.ForeignKey(Countries, verbose_name='الدولة',on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
  regionID = models.ForeignKey(States, verbose_name='المنطقة',on_delete=models.PROTECT, blank=True, null=True)
  stateID = models.ForeignKey(Region, verbose_name='الولاية',on_delete=models.PROTECT, blank=True, null=True)
  cityID = models.ForeignKey(Cities, verbose_name='المدينة',on_delete=models.PROTECT, blank=True, null=True)
  def __str__(self):
    return str(self.cycle_ar)

class ShareholdersInfo(models.Model):
  personID = models.OneToOneField(Person, related_name='personID', on_delete=models.CASCADE)
  marketerID = models.ForeignKey(EmpInfo, related_name='marketerID', verbose_name='المسووق',on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الموظف في حالة حذف المسوق
  def __str__(self):
    return str(self.personID)
  
class TypeContract(models.Model):
  typeContract_ar = models.CharField(verbose_name='نوع العقد عربي',max_length=100, blank=True, null=True)
  typeContract_en = models.CharField(verbose_name='نوع العقد إنجليزي',max_length=100, blank=True, null=True)

class Contracts(models.Model):
  shareholdersID = models.ForeignKey(ShareholdersInfo, related_name='Shareholders', verbose_name='المساهم', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
  dateOfContract = models.DateField(verbose_name='تاريخ العقد', blank=True, null=True)
  contractNumber = models.CharField(verbose_name='رقم العقد',max_length=100, blank=True, null=True)
  typeContractID = models.ForeignKey(TypeContract, verbose_name='نوع العقد', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
  cycleID = models.ForeignKey(Cycle, verbose_name='الدورة', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
  receiptID = models.ForeignKey(Qayd, verbose_name='رقم القيد', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
  numberOfShares = models.IntegerField(verbose_name='عدد الأسهم', default=1)
  amountOfShare = models.IntegerField(verbose_name='سعر السهم', default=1200000)
  profitRate = models.IntegerField(verbose_name='معدل الربح', default=8)
  dateOfDividend = models.DateField(verbose_name='تاريخ توزيع الأرباح', blank=True, null=True)
  witnes1ID = models.ForeignKey(EmpInfo, related_name='witnes1ID', verbose_name='الشاهد الأول',on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الموظف في حالة حذف المسوق
  witnes2ID = models.ForeignKey(EmpInfo, related_name='witnes2ID', verbose_name='الشاهد الثاني',on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الموظف في حالة حذف المسوق
  notes = models.TextField(verbose_name='ملاحظات', blank=True, null=True)
  def __str__(self):
    return str(self.shareholdersID)
  
    