from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import RepairTagAction


@receiver(post_save, sender=RepairTagAction)
def update_tag_status(sender, instance, **kwargs):
    tag = instance.tag
 

    if tag:
        if instance.status == "Completed":
            tag.status = "Completed"
        elif instance.status == "In Progress" and tag.status != "Completed":
            tag.status = "In Progress"
        else:
            tag.status = "Not Started"
        tag.save()
