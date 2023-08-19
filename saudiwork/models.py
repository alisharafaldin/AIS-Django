from django.db import models
from basicinfo.models import Person, LegalPersonality, WorkingStatus

# Create your models here.
class Company(models.Model):
    company = models.OneToOneField(LegalPersonality, on_delete=models.CASCADE)
    POBox = models.CharField(verbose_name='صندوق البري',max_length=100, blank=True, null=True)
    commercialRegister = models.CharField(verbose_name='السجل التجاري',max_length=100, blank=True, null=True)
    businessOfficeNo = models.CharField(verbose_name='مكتب العمل',max_length=100, blank=True, null=True)
    waselNo = models.CharField(verbose_name='واصل',max_length=100, blank=True, null=True)
    zakatAndIncomeNo = models.CharField(verbose_name='الزكاء والضريبة',max_length=100, blank=True, null=True)
    socialSecurityNo = models.CharField(verbose_name='التأمينات الاجتماعية',max_length=100, blank=True, null=True)
    chamberOfCommerceNo = models.CharField(verbose_name='الغرفة التجارية',max_length=100, blank=True, null=True)
    municipalAffairsNo = models.CharField(verbose_name='شؤون البلدية',max_length=100, blank=True, null=True)
    documentLink = models.CharField(verbose_name='رابط المستندات',max_length=100, blank=True, null=True)
    def __str__(self):
        return str(self.company)
    
class Sponser(models.Model):
    sponsName = models.CharField(verbose_name='إسم الكفيل', max_length=100)
    companyID = models.ForeignKey(Company, verbose_name='الشركة',on_delete=models.CASCADE) #لن يتم حزف الصنف في حالة حذف الموظف
    def __str__(self):
        return str(self.sponsName)

class EmpInfo(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    sponserID = models.ForeignKey(Sponser, verbose_name='الكفيل', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    workingStatusID = models.ForeignKey(WorkingStatus, verbose_name='حالة العمل', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
    passportNumber = models.CharField(verbose_name='رقم الجواز',max_length=100, blank=True, null=True)
    visaNumber = models.CharField(verbose_name='رقم التأشيرة',max_length=100, blank=True, null=True)
    passportExpiryDate = models.DateField(verbose_name='تاريخ إنتهاء الجواز', blank=True, null=True)
    medicalInsuranceExpirDate = models.DateField(verbose_name='تاريخ إنتهاء التأمين الطبي', blank=True, null=True)
    borderNumber = models.CharField(verbose_name='رقم الحدود',max_length=100, blank=True, null=True)
    enteryDate = models.DateField(verbose_name='تاريخ الدخول', blank=True, null=True) 
    businessOfficeNumber = models.CharField(verbose_name='رقم مكتب العمل',max_length=100, blank=True, null=True)
    iqamaNumber = models.CharField(verbose_name='رقم الإقامة',max_length=100, blank=True, null=True)
    iqamaExpiredDate = models.DateField(verbose_name='تاريخ إنتهاء الإقامة', blank=True, null=True)
    salaryInsurance = models.DecimalField(verbose_name="راتب التأمينات", default=400, decimal_places=2, max_digits=10, blank=True, null=True)
    contractSalary = models.DecimalField(verbose_name="راتب العقد", default=1200, decimal_places=2, max_digits=10, blank=True, null=True)
    fixedExtra = models.DecimalField(verbose_name="إضافي ثابت", default=0, decimal_places=2, max_digits=10, blank=True, null=True)
    iqamaReleaseDate = models.DateField(verbose_name='تاريخ إصدار الإقامة', blank=True, null=True)
    workStartingDate = models.DateField(verbose_name='تاريخ بداية العمل', blank=True, null=True)
    endDateOfService = models.DateField(verbose_name='تاريخ نهاية العمل', blank=True, null=True)
    coronaCheck = models.BooleanField(default=True, verbose_name="فحص كرونا", blank=True, null=True)
    tawaklna = models.BooleanField(default=True, verbose_name="توكلنا", blank=True, null=True)
    sahaty = models.BooleanField(default=True, verbose_name="صحتي", blank=True, null=True)
    medicalInsurance = models.BooleanField(default=True, verbose_name="تأمين طبي", blank=True, null=True)
    muqeemCopy = models.BooleanField(default=True, verbose_name="نسخة مقيم", blank=True, null=True)
    documentLink = models.CharField(verbose_name='رابط المستندات',max_length=100, blank=True, null=True)
    def __str__(self):
        return str(self.f_Name_ar)
    


