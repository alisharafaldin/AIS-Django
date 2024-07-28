from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin 
# Register your models here.

@admin.register(Project)
class ProjectImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar']

@admin.register(JobTitle)
class JobTitleImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar']

@admin.register(SubProject)
class SubProjectImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar']

@admin.register(CalendarYears)
class CalendarYearsImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'year']

@admin.register(CalendarMonths)
class CalendarMonthsImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar']

@admin.register(CalendarWeek)
class CalendarWeekImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar']

@admin.register(Gender)
class GenderImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar']

@admin.register(Cities)
class CitiesImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar', 'stateID', 'population']

@admin.register(Countries)
class CountriesImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar']

@admin.register(TypeAccBank)
class TypeAccBankImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar']

@admin.register(BranchBank)
class BranchBankImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar', 'name_en', 'bankID', 'name_Symbol']

@admin.register(TypeID)
class TypeIDImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar']

@admin.register(TypeTransaction)
class TypeTransactionImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar']

@admin.register(Region)
class RegionImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'countryID', 'name_ar', 'capitalRegion']

@admin.register(States)
class statesImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'regionID', 'name_ar', 'capitalState', 'population']

@admin.register(SocialStatus)
class RSocialStatusImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar']

@admin.register(WorkTrade)
class WorkTradeTypeImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar']

@admin.register(Bank)
class BankImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar', 'name_Symbol']

@admin.register(WorkSpecialty)
class WorkSpecialtyTypeImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar']

@admin.register(WorkingStatus)
class WorkingStatusImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar']

@admin.register(Person)
class PersonImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'f_Name_ar', 's_Name_ar', 't_Name_ar']

