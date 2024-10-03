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

@admin.register(BusinessType)
class BusinessTypeImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar']
    
@admin.register(BusinessScope)
class BusinessScopeImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar']
    
@admin.register(BusinessScopeSpecialization)
class BusinessScopeSpecializationImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar', 'businessScopeID']
    
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

@admin.register(Size)
class SizeImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name']

@admin.register(TargetGroup)
class TargetGroupImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar']

@admin.register(Color)
class ColorImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar']

@admin.register(Skills)
class SkillsImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar']

@admin.register(Languages)
class LanguagesImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar']

@admin.register(TypeDelivery)
class TypeDeliveryImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar']

@admin.register(TypePayment)
class TypePaymentImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar']

@admin.register(TypeUnit)
class TypeUnitImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar']

@admin.register(BasicInfo)
class BasicInfoImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'attachments', 'nationalityID', 'countryID', 'regionID', 'stateID', 'cityID', 'address', 'phone', 'phoneOther']

@admin.register(LegalPersons)
class LegalPersonsImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'basicInfoID', 'name_ar', 'businessTypeID']

@admin.register(Persons)
class PersonImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'basicInfoID', 'f_Name_ar', 's_Name_ar', 't_Name_ar']


