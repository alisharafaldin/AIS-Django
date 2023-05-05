from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin 

# Register your models here.
@admin.register(Currency)
class CurrencyImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id','currency_ar','currency_en','currencyCode']

@admin.register(AccType)
class AccTypeImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id','accType_ar']

@admin.register(AccDorC)
class AccDorCImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id','accDorC_ar']

@admin.register(AccBudget)
class AccBudgetImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id','accBudget_ar']

@admin.register(AccountsTree)
class AccountsTreeImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'accName_ar']

@admin.register(Qayd)
class QaydImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id']

@admin.register(QaydDetails)
class QaydDetailsImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id']



