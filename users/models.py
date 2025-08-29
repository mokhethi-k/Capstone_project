import os
from django.db import models
from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible
 

class Department(models.Model):
    name = models.CharField(max_length=100) 
    manager = models.OneToOneField("Profile", on_delete=models.SET_NULL, null=True, limit_choices_to={'specialization': 'manager'}, related_name='managed_department')


    def __str__(self):
        return self.name


@deconstructible
class ProfilePicturePath(object):
    def __init__(self):
        pass

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        path = f'accounts/media/{instance.user.id}/images'
        name = f'profile_picture.{ext}'
        
        return os.path.join(path, name)
    
profile_picture_path = ProfilePicturePath()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1, related_name='members')
    category = [
        ('manager', 'Manager',),
        ('engineer', 'Engineer'),
        ('supervisor', 'Supervisor'),
        ('technician', 'Technician'),
        ('artisan', 'Artisan'),
        ('operator', 'Operator'),
        ('contractor', 'Contractor'),
    ]
    specialization = models.CharField(max_length=100, choices=category, default='Operator')
    position = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    profile_picture = models.FileField(upload_to=profile_picture_path, blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}"
    





