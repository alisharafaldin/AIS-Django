from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin 
# Register your models here.

@admin.register(ItemType)
class CategoryTypeImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'companyID', 'sequence', 'name_ar', 'name_en']

@admin.register(ItemGrop)
class CategoryImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar', 'name_en', 'itemTypeID']

@admin.register(Item)
class ItemsImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar', 'name_en', 'itemGropID']

@admin.register(ItemDetails)
class ItemsDetailsImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'itemID', 'colorID', 'sizeID', 'description', 'photo']

