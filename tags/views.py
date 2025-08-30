from rest_framework import viewsets, permissions
from .models import RepairTag
from .serializers import RepairTagSerializer
from users.models import Profile

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Count


class RepairTagViewSet(viewsets.ModelViewSet):
    queryset = RepairTag.objects.all().order_by('-created_at')
    serializer_class = RepairTagSerializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    

    def get_queryset(self):
        user = self.request.user

        # Superusers see everything
        if user.is_superuser:
            return RepairTag.objects.all()

        # Normal users see only their department’s tags
        if hasattr(user, "profile") and user.profile.department:
            return RepairTag.objects.filter(department=user.profile.department)

        # Fallback: if user has no profile/department
        return RepairTag.objects.none()

    def perform_create(self, serializer):
        """Auto-assign department + creator when a user creates a tag"""
        serializer.save(
            created_by=self.request.user,
            department=self.request.user.profile.department
        )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_stats(request):
    user = request.user

    # base queryset restricted by department
    if user.is_superuser:
        qs = RepairTag.objects.all()
    elif hasattr(user, "profile") and user.profile.department:
        qs = RepairTag.objects.filter(department=user.profile.department)
    else:
        qs = RepairTag.objects.none()

    stats = {
        "total_tags": qs.count(),
        "status_breakdown": qs.values("status").annotate(count=Count("id")),
        "priority_breakdown": qs.values("priority").annotate(count=Count("id")),
        "repair_type_breakdown": qs.values("repair_type").annotate(count=Count("id")),
    }

    return Response(stats)