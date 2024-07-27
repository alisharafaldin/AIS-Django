from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from mptt.admin import DraggableMPTTAdmin

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

@admin.register(AccountsTree)
class AccountsTreeAdmin(DraggableMPTTAdmin, ImportExportModelAdmin):
    list_display = ('tree_actions', 'indented_title', 'id', 'name_ar', 'typeID', 'natureID', 'categoryID', 'code', 'description', 'is_can_pay', 'parent')
    list_display_links = ('indented_title',)

# admin.site.register(AccountsTree, AccountsTreeAdmin)

@admin.register(QaydDetails)
class QaydDetailsImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id' , 'qaydID' , 'description_details' , 'date_details' , 'debit' , 'credit']

class QaydDetailsInline(admin.TabularInline):
    model = QaydDetails
    extra = 1


class QaydAdmin(admin.ModelAdmin):
    list_display = ('id', 'companyID', 'sequence', 'created_by')
    inlines = [QaydDetailsInline]  # إذا كنت بحاجة إلى إدراج `QaydDetailsInline`

# تسجيل نموذج `Qayd` باستخدام `QaydAdmin` فقط مرة واحدة
admin.site.register(Qayd, QaydAdmin)
# admin.site.unregister(User)
# admin.site.register(User, BaseUserAdmin)




