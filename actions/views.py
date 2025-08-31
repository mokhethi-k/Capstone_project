from rest_framework import viewsets, permissions
from .models import RepairTagAction
from .serializers import RepairTagActionSerializer


class RepairTagActionViewSet(viewsets.ModelViewSet):
    queryset = RepairTagAction.objects.all().order_by('-created_at')
    serializer_class = RepairTagActionSerializer
    permission_classes = [permissions.IsAuthenticated]
