from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin 

# Register your models here.

@admin.register(AccountType)
class AccountTypeImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id']

@admin.register(AccountNature)
class AccountNatureImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id']

@admin.register(AccountCategory)
class AccountCategoryImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id']

@admin.register(AccountsTree)
class AccountsTreeImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id']

@admin.register(Qayd)
class QaydImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id']

@admin.register(QaydDetails)
class QaydDetailsImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id']




