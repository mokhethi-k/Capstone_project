from rest_framework import serializers
from .models import RepairTagAction


class RepairTagActionSerializer(serializers.ModelSerializer):
    action = serializers.ReadOnlyField(source='tag.action')
    assigned_by = serializers.ReadOnlyField(source='assigned_by.username')
    class Meta:
        model = RepairTagAction
        fields = ['id', 'url', 'action', 'assigned_to', 'assigned_by', 'evidence', 'evidence_file', 'evidence_image', 'status', 'complete_at', 'created_at']

        read_only_fields = ('assigned_by', 'created_at', 'complete_at')


        def create(self, validated_data):
            tag = validated_data['tag']
            validated_data['assigned_by'] = tag.created_by
            return super().create(validated_data)
