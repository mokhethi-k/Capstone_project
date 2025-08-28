
from actions.models import RepairTagAction
from django.conf import settings
from .models import RepairTag
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=RepairTag)
def create_initial_action(sender, instance, created, **kwargs):
    if created and instance.assigned_to:
        RepairTagAction.objects.create(
            tag=instance,
            assigned_to=instance.assigned_to,  #link to chosen user
            status='Not Started'
        )