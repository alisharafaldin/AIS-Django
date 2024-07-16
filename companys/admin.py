from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin 
# Register your models here.


@admin.register(BusinessType)
class BusinessTypeImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar']

@admin.register(Company)
class CompanyImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar']

@admin.register(CompanyUser)
class CompanyUserImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id','userID', 'companyID', 'jobTitleID']



