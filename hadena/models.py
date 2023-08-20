
from django.db import models
from datetime import date 
from employees.models import EmpInfo
from basicinfo.models import  Countries, Region, States, Cities, Person

class Axis(models.Model):
    axis_ar = models.CharField(verbose_name='المحور عربي',max_length=100)
    axis_er = models.CharField(verbose_name='المحور إنجليزي',max_length=100, blank=True, null=True)
    directSupervisor = models.CharField(verbose_name='المشرف المباشر',max_length=100, blank=True, null=True)
    phoneDirectSupervisor = models.CharField(verbose_name='جوال المشرف المباشر',max_length=100, blank=True, null=True)
    countryID = models.ForeignKey(Countries, verbose_name='الدولة',on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    regionID = models.ForeignKey(States, verbose_name='المنطقة',on_delete=models.PROTECT, blank=True, null=True)
    stateID = models.ForeignKey(Region, verbose_name='الولاية',on_delete=models.PROTECT, blank=True, null=True)
    cityID = models.ForeignKey(Cities, verbose_name='المدينة',on_delete=models.PROTECT, blank=True, null=True)
    def __str__(self):
        return str(self.axis_ar)

class ShareholdersInfo(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    marketerID = models.ForeignKey(EmpInfo , verbose_name='المسووق',on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الموظف في حالة حذف المسوق
    def __str__(self):
        return str(self.f_Name_ar) + " " + str(self.s_Name_ar)

class Contracts(models.Model):
    shareholdersID = models.ForeignKey(ShareholdersInfo, related_name='Shareholders', verbose_name='المساهم', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    dateOfContract = models.DateField(verbose_name='تاريخ العقد', blank=True, null=True)
    contractNumber = models.CharField(verbose_name='رقم العقد',max_length=100, blank=True, null=True)
    axisID = models.ForeignKey(Axis, verbose_name='المحور', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    numberReceipt = models.CharField(verbose_name='رقم الإيصال',max_length=100, blank=True, null=True)
    numberOfShares = models.IntegerField(verbose_name='عدد الأسهم', default=1)
    amountOfShare = models.IntegerField(verbose_name='سعر السهم', default=1200000)
    profitOfShare = models.IntegerField(verbose_name='ربح السهم', default=8)
    dateOfDividend = models.DateField(verbose_name='تاريخ توزيع الأرباح', blank=True, null=True)
    witnes1ID = models.ForeignKey(EmpInfo ,related_name='witnes1ID', verbose_name='الشاهد الأول',on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الموظف في حالة حذف المسوق
    Witnes2ID = models.ForeignKey(EmpInfo ,related_name='Witnes2ID', verbose_name='الشاهد الثاني',on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الموظف في حالة حذف المسوق
    def __str__(self):
        return str(self.shareholdersID)
    
    