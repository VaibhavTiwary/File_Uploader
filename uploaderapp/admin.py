from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import FileData

admin.register(FileData)


class DataAdmin(ImportExportModelAdmin):
    list_display = ("date", "accno", "custPin", "dpd")
