from rest_framework import viewsets, permissions
from .models import RepairTag
from .serializers import RepairTagSerializer


class RepairTagViewSet(viewsets.ModelViewSet):
    queryset = RepairTag.objects.all().order_by('-created_at')
    serializer_class = RepairTagSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        """
        Automatically set created_by to the current user
        """
        serializer.save(created_by=self.request.user)