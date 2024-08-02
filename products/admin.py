from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin 
# Register your models here.

@admin.register(ItemType)
class CategoryTypeImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar', 'name_en']

@admin.register(ItemGrop)
class CategoryImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'name_ar', 'name_en', 'itemTypeID']

@admin.register(ItemDetails)
class ItemsDetailsImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'itemGropID' , 'purchasingPrice', 'sellingPrice', 'name_en', 'colorID', 'sizeID', 'description', 'photo']

