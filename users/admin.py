from django.contrib import admin
from .models import Department, Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'department', 'specialization', 'position', 'phone_number']


admin.site.register(Department)
admin.site.register(Profile, ProfileAdmin)