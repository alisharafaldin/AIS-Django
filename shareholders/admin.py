from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin 

# Register your models here.

@admin.register(Contracts)
class ContractsImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'shareholdersID']

@admin.register(ShareholdersInfo)
class ShareholdersInfoImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'f_Name_ar']


@admin.register(Axis)
class AxisImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'axis_ar']

