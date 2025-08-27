from rest_framework import viewsets
from .models import RepairTagAction
from .serializers import RepairTagActionSerializer


class RepairTagActionViewSet(viewsets.ModelViewSet):
    queryset = RepairTagAction.objects.all().order_by('-created_at')
    serializer_class = RepairTagActionSerializer

