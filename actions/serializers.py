from rest_framework import serializers
from .models import RepairTagAction


class RepairTagActionSerializer(serializers.ModelSerializer):
    action = serializers.ReadOnlyField(source='tag.action')
    assigned_by = serializers.ReadOnlyField(source='assigned_by.username')
    class Meta:
        model = RepairTagAction
        fields = ['id', 'url', 'action', 'assigned_to', 'assigned_by', 'evidence', 'evidence_file', 'evidence_image', 'status', 'complete_at', 'created_at']

        read_only_fields = ('created_at', 'complete_at', 'assigned_by')


    def validate_assigned_to(self, value):
        """Ensure assigned user is in the same department as the tag creator"""
        tag_creator = self.context.get('assigned_by')
        if tag_creator and value.profile.department != tag_creator.profile.department:
            raise serializers.ValidationError(
                "You can only assign actions to users in your department."
            )
        return value

    def create(self, validated_data):
        user = self.context.get('assigned_by')
        if user:
            validated_data['assigned_by'] = user
        return super().create(validated_data)
