from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin 

# Register your models here.

@admin.register(AccountType)
class AccountTypeImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id','Type_ar']

@admin.register(AccountNature)
class AccountNatureImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id','nature_ar']

@admin.register(AccountBudget)
class AccountBudgetImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id','budget_ar']

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




