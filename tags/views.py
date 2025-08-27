from rest_framework import viewsets
from .models import RepairTag
from .serializers import RepairTagSerializer


class RepairTagViewSet(viewsets.ModelViewSet):
    queryset = RepairTag.objects.all().order_by('-created_at')
    serializer_class = RepairTagSerializer
    
