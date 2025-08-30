from django.contrib import admin
from .models import RepairTag
from django.contrib.auth.models import User

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

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "assigned_to" and not request.user.is_superuser:
            if hasattr(request.user, "profile") and request.user.profile.department:
                kwargs["queryset"] = User.objects.filter(profile__department=request.user.profile.department)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(RepairTag, RepairTagAdmin)