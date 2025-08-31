from django.contrib import admin
from .models import RepairTagAction

class RepairTagAdmin(admin.ModelAdmin):
    list_display = ['tag', 'assigned_by', 'assigned_to',  'created_at', 'status', 'complete_at']
    readonly_fields = ('assigned_to', 'assigned_by')
     

admin.site.register(RepairTagAction, RepairTagAdmin)