from django.contrib import admin
from .models import RepairTag
from django.contrib.auth.models import User

# Register your models here.

class RepairTagAdmin(admin.ModelAdmin):
    list_display = ['action', 'repair_type', 'created_by', 'area_found', 'priority', 'status', 'created_at', 'deadline']
    readonly_fields = ('status',)


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if hasattr(request.user, "profile") and request.user.profile.department:
            return qs.filter(department=request.user.profile.department)
        return qs.none()


admin.site.register(RepairTag, RepairTagAdmin)