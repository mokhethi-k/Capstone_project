from django.contrib import admin
from .models import Department, Profile


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'manager')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "manager":
            kwargs["queryset"] = Profile.objects.filter(specialization="manager")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'user__email', 'specialization']
    list_display = ['user', 'department', 'specialization', 'position', 'phone_number']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Department, DepartmentAdmin)