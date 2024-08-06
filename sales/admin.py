from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin 
# Register your models here.

@admin.register(Customers)
class CustomersImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'legalPersonID']

@admin.register(InvoicesSalesHead)
class InvoicesSalesHeadImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'supplierID']

@admin.register(InvoicesSalesBody)
class InvoicesSalesBodyImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'itemID', 'quantity', 'unit_price', 'discount', 'total_price_before_tax']