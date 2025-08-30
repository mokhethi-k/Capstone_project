from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import RepairTagAction
from django.core.mail import send_mail
from django.conf import settings


@receiver([post_save, post_delete], sender=RepairTagAction)
def update_tag_status(sender, instance, **kwargs):
    tag = instance.tag
    actions = tag.actions.all()

    if actions.filter(status="In Progress").exists():
        tag.status = "In Progress"
    elif actions.filter(status="Not Started").exists():
        tag.status = "Not Started"
    elif actions.exists():
        tag.status = "Completed"
    else:
        tag.status = "Not Started"  # no actions left

    tag.save()



@receiver(post_save, sender=RepairTagAction)
def send_assignment_email(sender, instance, created, **kwargs):
    if created and instance.assigned_to and instance.assigned_to.email:
        # API URL to the action
        action_api_url = f"{settings.SITE_URL}/api/actions/{instance.id}/"

        # Email content
        subject = f"New Repair Action Assigned - Tag {instance.tag.id}"
        message = (
            f"Dear {instance.assigned_to.username},\n\n"
            f"You have been assigned a new action for Repair Tag {instance.tag.id}.\n"
            f"Status: {instance.status}\n"
            f"Deadline: {instance.tag.deadline}\n\n"
            f"View action details here (API): {action_api_url}\n\n"
            f"Please check the system for more details."
        )

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [instance.assigned_to.email],
            fail_silently=False
        )