
from rest_framework import serializers
from .models import RepairTag
from actions.serializers import RepairTagActionSerializer
from actions.models import RepairTagAction
from django.contrib.auth.models import User

class RepairTagSerializer(serializers.ModelSerializer):
    actions = RepairTagActionSerializer(many=True, required=False)
    status = serializers.CharField(read_only=True)
    created_by = serializers.ReadOnlyField(source='created_by.username')  
    class Meta:
        model = RepairTag
        fields = ['id', 'url', 'department', 'created_by', 'area_found', 'repair_type', 
                  'action', 'assigned_to', 'priority', 'created_at', 'deadline', 'status', 'actions']

    def create(self, validated_data):
        request = self.context.get("request")
        user = getattr(request, 'user', None)  # safer access

        # Set the creator of the tag
        validated_data['created_by'] = user

        # Extract nested actions
        actions_data = validated_data.pop('actions', [])

        # Create the tag
        repair_tag = RepairTag.objects.create(**validated_data)

        # Create nested actions with assigned_by set automatically
        for action_data in actions_data:
            RepairTagAction.objects.create(tag=repair_tag, assigned_by=user, **action_data)

            # Pass 'assigned_by' via context
            serializer = RepairTagActionSerializer(
                data=action_data, 
                context={'assigned_by': user}
                )
            serializer.is_valid(raise_exception=True)
            serializer.save(tag=repair_tag)

        return repair_tag
    

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return RepairTag.objects.all()
        elif hasattr(user, "profile") and user.profile.department:
            return RepairTag.objects.filter(department=user.profile.department)
        else:
            return RepairTag.objects.none()
