from django.contrib import admin
from .models import *
# Register your models here.
class SettingsAdmin(admin.ModelAdmin):  
    list_display = (
        "id",
        "email",
    )
admin.site.register(Settings,SettingsAdmin)
