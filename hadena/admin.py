from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin 

# Register your models here.
@admin.register(ShareholdersInfo)
class ShareholdersInfoImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id']

@admin.register(Contracts)
class ContractsImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id']


@admin.register(Cycle)
class CycleImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id']

