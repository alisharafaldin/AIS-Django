from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# from .resources import CustomerResource
# Register your models here.

# @admin.register(Customers)
# class CustomerAdmin(ImportExportModelAdmin):
# resource_class = CustomerResource

@admin.register(Customers)
class CustomersImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'legalPersonID']

@admin.register(Inventory)
class InventoryImportE(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar']

@admin.register(InvoicesSalesBody)
class InvoicesSalesBodyImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'invoiceHeadID', 'itemID', 'quantity', 'unit_price', 'discount', 'total_price_before_tax', 'total_price_local_currency', 'tax_rate', 'tax_value', 'total_price_after_tax']

class InvoicesSalesBodyInline(admin.TabularInline):
    model = InvoicesSalesBody
    extra = 1

class InvoicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'companyID', 'sequence', 'created_by')
    inlines = [InvoicesSalesBodyInline]  # إذا كنت بحاجة إلى إدراج `QaydDetailsInline`

# تسجيل نموذج `Qayd` باستخدام `QaydAdmin` فقط مرة واحدة
# admin.site.register(InvoicesSalesHead, InvoicesAdmin)

@admin.register(InvoicesSalesHead)
class InvoicesSalesHeadImportE(ImportExportModelAdmin):
    pass
    list_display = ['id', 'typeTransactionID']