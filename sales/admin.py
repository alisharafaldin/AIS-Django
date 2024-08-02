from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin 
# Register your models here.

@admin.register(Customers)
class SuppliersImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'legalPersonsID']

@admin.register(SalesInvoiceHead)
class InvoiceHeadImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'supplierID']

@admin.register(SalesInvoiceBody)
class InvoiceBodyImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'itemsDetailstID', 'quantity', 'unit_price', 'discount', 'total_price_before_tax']


