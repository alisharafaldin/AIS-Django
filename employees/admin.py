from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin 

# Register your models here.

# admin.site.register(Cities)
@admin.register(Cities)
class CitiesImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'cityName_ar']

@admin.register(Countries)
class CountriesImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'countryName_ar']

@admin.register(TypeAccBank)
class TypeAccBankImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'TypeAccBank_AR']

@admin.register(BranchBank)
class BranchBankImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'branchBank_AR']

@admin.register(TypeID)
class TypeIDImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'typeID_ar']

@admin.register(Company)
class CompanyImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'compName_ar']

@admin.register(Region)
class RegionImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'RegionName_ar']

@admin.register(States)
class statesImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'stateName_ar']

@admin.register(SocialStatus)
class RSocialStatusImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'socialStatus_ar']

@admin.register(BusinessType)
class BusinessTypeImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'type_ar']

@admin.register(WorkTrade)
class WorkTradeTypeImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'workTrade_ar']

@admin.register(Bank)
class BankImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'bank_ar', 'bank_Symbol']

@admin.register(WorkSpecialty)
class WorkSpecialtyTypeImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'workSpecialty_ar']

@admin.register(WorkingStatus)
class WorkingStatusImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'workingStatus_ar']

@admin.register(EmpInfo)
class EmpInfoImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'f_Name_ar' , 's_Name_ar', 'sponserID', 'companyID', 'enteryDate']

# admin.site.register(EmpInfo)

@admin.register(Sponser)
class SponserImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'sponsName']

@admin.register(Project)
class ProjectImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'proName_ar']

@admin.register(SubProject)
class SubProjectImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'subProName_ar']

@admin.register(CalendarYears)
class CalendarYearsImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'year']

@admin.register(CalendarMonths)
class CalendarMonthsImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'month_ar', 'month_en_sort', 'daysOfMonth']

@admin.register(CalendarWeek)
class CalendarWeekImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'day_ar']

@admin.register(Gender)
class GenderImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'gender_ar']

@admin.register(ProjectRotation)
class ProjectRotationImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'empID', 'projectID', 'subProjectID']

# @admin.register()
# class ImportExport(ImportExportModelAdmin):
#     pass
#     list_display = ['id', '']