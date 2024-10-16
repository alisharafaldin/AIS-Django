from .models import *
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

@admin.register(Customers)
class CustomersImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'legalPersonID']

@admin.register(InvoicesSalesBody)
class InvoicesSalesBodyImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'invoiceHeadID', 'inventoryID', 'itemID', 'quantity', 'unit_price', 'discount', 'total_price_before_tax', 'total_price_local_currency', 'tax_rate', 'tax_value', 'total_price_after_tax']

class InvoicesSalesBodyInline(admin.TabularInline):
    model = InvoicesSalesBody
    extra = 1

class InvoicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'companyID', 'sequence', 'created_by')
    inlines = [InvoicesSalesBodyInline]  # إذا كنت بحاجة إلى إدراج `QaydDetailsInline`

@admin.register(InvoicesSalesHead)
class InvoicesSalesHeadImportE(ImportExportModelAdmin):
    pass
    list_display = ['id', 'sequence', 'attachments', 'total_price_after_tax', 'date', 'typeTransactionID', 'customerID', 'inventoryID', 'currencyID', 'rate']