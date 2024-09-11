from django.db import models
from datetime import date 
from basicinfo.models import LegalPersons, JobTitle
from django.contrib.auth.models import User


class Company(models.Model):
    owner = models.ForeignKey(User, verbose_name='المالك', on_delete=models.PROTECT, related_name='owner_companies', blank=True)
    legalPersonID = models.OneToOneField(LegalPersons, related_name="company", on_delete=models.CASCADE, blank=True)
    isDelivery = models.BooleanField(default=True, verbose_name="يوجد توصيل", blank=True, null=True)
    includeInDalilAlaemal = models.BooleanField(default=True, verbose_name="تضمين في دليل الأعمال", blank=True, null=True)
    includeInInAccountingRecords = models.BooleanField(default=False, verbose_name="تضمين في السجلات المحاسبية", blank=True, null=True)
    def __str__(self):
        return str(self.legalPersonID)

class CompanyUser(models.Model):
    companyID = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='companys')
    userID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='company_users')
    jobTitleID = models.ForeignKey(JobTitle, on_delete=models.CASCADE, verbose_name='المسمى الوظيفي',)  # مثلا: 'Admin', 'Editor', etc.

    class Meta:
        unique_together = ('userID', 'companyID')

    def __str__(self):
        return f"{self.userID} - {self.companyID}"