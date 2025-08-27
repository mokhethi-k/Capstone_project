
from actions.models import RepairTagAction
from django.conf import settings
from .models import RepairTag
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=RepairTag)
def create_default_action(sender, instance, created, **kwargs):
    if created:
        RepairTagAction.objects.create(
            tag=instance,
            assigned_by=instance.created_by,
            assigned_to=instance.created_by,  # can later be reassigned
            status="Not Started"
        )