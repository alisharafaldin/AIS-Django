from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin 
# Register your models here.

@admin.register(Company)
class CompanyImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'owner', 'legalPersonID']

@admin.register(CompanyUser)
class CompanyUserImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id','userID', 'companyID', 'jobTitleID']



