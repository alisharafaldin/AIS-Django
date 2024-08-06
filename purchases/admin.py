from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin 
# Register your models here.

@admin.register(Suppliers)
class SuppliersImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'legalPersonID']

@admin.register(InvoiceHead)
class InvoiceHeadImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'supplierID']

@admin.register(InvoiceBody)
class InvoiceBodyImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'itemID', 'quantity', 'unit_price', 'discount', 'total_price_before_tax']


