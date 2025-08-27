from django.db import models
from django.contrib.auth.models import User
from users.models import Department


class RepairTag(models.Model):

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Critical', 'Critical'),
    ]

    STATUS_CHOICES = [
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    REPAIR_TYPE_CHOICES = [
        ('Preventive', 'Preventive'),
        ('Corrective', 'Corrective'),
        ('Predictive', 'Predictive'),
    ]

   
    department = models.ForeignKey(
        Department, 
        on_delete=models.CASCADE,
        related_name='repair_tags'
    )
    created_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_tags'
    )
    area_found = models.CharField(max_length=255)
    repair_type = models.CharField(max_length=50, choices=REPAIR_TYPE_CHOICES)
    reason = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not Started')

    def __str__(self):
        return f"{self.reason} ({self.status})"

