from django.contrib import admin
from .models import Department, Profile


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    autocomplete_fields = ['manager']

class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'user__email', 'specialization']
    list_display = ['user', 'department', 'specialization', 'position', 'phone_number']

admin.site.register(Profile, ProfileAdmin)