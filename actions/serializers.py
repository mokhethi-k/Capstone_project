from rest_framework import serializers
from .models import RepairTagAction


class RepairTagActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairTagAction
        fields = ['id', 'url', 'assigned_to', 'assigned_by', 'evidence', 'status', 'complete_at', 'created_at']

