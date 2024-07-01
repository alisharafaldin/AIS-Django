from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin 

# Register your models here.
@admin.register(Album)
class AlbumImportExport(ImportExportModelAdmin):
    pass
    list_display = ['name']

@admin.register(Posts)
class PostsImportExport(ImportExportModelAdmin):
    pass
    list_display = ['title']