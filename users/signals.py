from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Profile

#This function enable automatic user profile creation
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#This function enables unique username creation in case the first and last names already exists
@receiver(pre_save, sender=User)
def create_username(sender, instance, **kwargs):
    if not instance.username:
        username = f'{instance.first_name[0]}_{instance.last_name}'.lower()
        counter = 1
        while User.objects.filter(username=username):
            username = f'{instance.first_name[0]}_{instance.last_name}{counter}'.lower()
            counter += 1
        instance.username = username