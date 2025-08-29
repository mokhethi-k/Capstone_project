from django.contrib import admin
from .models import RepairTag
from users.models import Profile

# Register your models here.

class RepairTagAdmin(admin.ModelAdmin):
    list_display = ['repair_type', 'action', 'area_found', 'priority', 'status', 'created_at', 'deadline']
    readonly_fields = ('status',)


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if hasattr(request.user, "profile") and request.user.profile.department:
            return qs.filter(department=request.user.profile.department)
        return qs.none()

    def save_model(self, request, obj, form, change):
        """Auto-assign department + creator when saving in admin"""
        if not change:  # when creating new
            obj.created_by = request.user
            if hasattr(request.user, "profile"):
                obj.department = request.user.profile.department
        super().save_model(request, obj, form, change)

admin.site.register(RepairTag, RepairTagAdmin)