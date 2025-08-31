from django.db import models
from django.contrib.auth.models import User
from tags.models import RepairTag  


class RepairTagAction(models.Model):
    STATUS_CHOICES = [
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    id = models.AutoField(primary_key=True)
    tag = models.ForeignKey(
        RepairTag,
        on_delete=models.CASCADE,
        related_name="actions"
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="assigned"
    )
    assigned_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="created_actions"
    )
    evidence = models.TextField(blank=True, null=True)  
    evidence_file = models.FileField(upload_to="evidence/", blank=True, null=True)
    evidence_image = models.ImageField(upload_to="evidence/images/", blank=True, null=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Not Started")
    created_at = models.DateTimeField(auto_now_add=True)
    complete_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Action for Tag {self.tag.id} - {self.status}"

