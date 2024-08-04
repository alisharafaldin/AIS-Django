from django.db import models
from datetime import date 
from basicinfo.models import LegalPersons, JobTitle
from django.contrib.auth.models import User


class Company(models.Model):
    owner = models.ForeignKey(User, verbose_name='المالك', on_delete=models.PROTECT, related_name='owner_companies', blank=True)
    legalPersonID = models.OneToOneField(LegalPersons, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return str(self.owner)

class CompanyUser(models.Model):
    companyID = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='companys')
    userID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='company_users')
    jobTitleID = models.ForeignKey(JobTitle, on_delete=models.CASCADE, verbose_name='المسمى الوظيفي',)  # مثلا: 'Admin', 'Editor', etc.

    class Meta:
        unique_together = ('userID', 'companyID')

    def __str__(self):
        return f"{self.userID} - {self.companyID}"