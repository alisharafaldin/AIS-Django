from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin 
# Register your models here.

@admin.register(Suppliers)
class SuppliersImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'legalPersonID']

@admin.register(InvoicesPurchasesHead)
class InvoicesPurchasesHeadImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'sequence', 'attachments', 'total_price_after_tax', 'supplierID']

@admin.register(InvoicesPurchasesBody)
class InvoicesPurchasesBodyImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'inventoryID', 'invoiceHeadID', 'itemID', 'quantity', 'unit_price', 'discount', 'total_price_before_tax']


