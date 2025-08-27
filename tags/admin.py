from django.contrib import admin
from .models import RepairTag

# Register your models here.

class RepairTagAdmin(admin.ModelAdmin):
    list_display = ['repair_type', 'action', 'area_found', 'priority', 'status', 'created_at', 'deadline']

admin.site.register(RepairTag, RepairTagAdmin)