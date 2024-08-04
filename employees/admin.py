from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin 

# Register your models here.

# admin.site.register(Cities)
@admin.register(EmployeeInfo)
class EmpInfoImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id']

# admin.site.register(EmpInfo)
@admin.register(ProjectRotation)
class ProjectRotationImportExport(ImportExportModelAdmin):
    pass
    list_display = ['id', 'empID', 'projectID', 'subProjectID']
