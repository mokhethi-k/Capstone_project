from django.contrib import admin
from .models import RepairTagAction

class RepairTagAdmin(admin.ModelAdmin):
    list_display = ['tag', 'assigned_to', 'assigned_by',  'created_at', 'status', 'complete_at']
     

admin.site.register(RepairTagAction, RepairTagAdmin)