
from rest_framework import serializers
from .models import RepairTag
from actions.serializers import RepairTagActionSerializer
from actions.models import RepairTagAction
from django.contrib.auth.models import User

class RepairTagSerializer(serializers.ModelSerializer):
    actions = RepairTagActionSerializer(many=True, required=False)

    class Meta:
        model = RepairTag
        fields = ['id', 'url', 'department', 'area_found', 'repair_type', 
                  'action', 'priority', 'created_at', 'deadline', 'status', 'actions']

    def create(self, validated_data):
  
        actions_data = validated_data.pop('actions', [])
        
        
        repair_tag = RepairTag.objects.create(**validated_data)
        
        
        for action_data in actions_data:
            RepairTagAction.objects.create(tag=repair_tag, **action_data)

        return repair_tag
