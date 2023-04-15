from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Dato

# Register your models here.

@admin.register(Dato)
class DatoAdmin(ImportExportModelAdmin):
    pass


