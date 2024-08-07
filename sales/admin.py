from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin 
# Register your models here.

@admin.register(Customers)
class CustomersImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'legalPersonID']

@admin.register(InvoicesSalesBody)
class InvoicesSalesBodyImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'itemID', 'quantity', 'unit_price', 'discount', 'total_price_before_tax', 'tax_rate', 'tax_value', 'total_price_after_tax']

class InvoicesSalesBodyInline(admin.TabularInline):
    model = InvoicesSalesBody
    extra = 1


class InvoicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'companyID', 'sequence', 'created_by')
    inlines = [InvoicesSalesBodyInline]  # إذا كنت بحاجة إلى إدراج `QaydDetailsInline`

# تسجيل نموذج `Qayd` باستخدام `QaydAdmin` فقط مرة واحدة
admin.site.register(InvoicesSalesHead, InvoicesAdmin)
# أو هذا الكود
# @admin.register(InvoicesSalesHead)
# class InvoicesSalesHeadImportExport(ImportExportModelAdmin):
#     pass
#     list_display = ['id', 'customerID']