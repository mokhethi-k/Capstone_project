from rest_framework import serializers
from .models import RepairTagAction


class RepairTagActionSerializer(serializers.ModelSerializer):
    action = serializers.ReadOnlyField(source='tag.action')
    class Meta:
        model = RepairTagAction
        fields = ['id', 'url', 'action', 'assigned_to', 'assigned_by', 'evidence', 'status', 'complete_at', 'created_at']

        read_only_fields = ('assigned_by', 'created_at', 'complete_at')
