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

@admin.register(AccountStatement)
class AccountStatementImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id']

@admin.register(AccountCategory)
class AccountCategoryImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id']

# @admin.register(AccountsTree)
# class AccountsTreeImportExport(ImportExportModelAdmin):
#     pass
#     list_display = ['id']

@admin.register(TypeTransaction)
class TypeTransactionImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id']

# @admin.register(Qayd)
# class QaydImportExport(ImportExportModelAdmin):
#     pass
#     list_display = ['id']

@admin.register(QaydDetails)
class QaydDetailsImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id' , 'qaydID' , 'description_details' , 'date_details' , 'debit' , 'credit']

class QaydDetailsInline(admin.TabularInline):
    model = QaydDetails
    extra = 1

class QaydAdmin(admin.ModelAdmin):
    inlines = [QaydDetailsInline]

admin.site.register(Qayd, QaydAdmin)
admin.site.register(AccountsTree)




