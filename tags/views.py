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

    # Base queryset restricted by department for non-superusers
    if user.is_superuser:
        qs = RepairTag.objects.all()
    elif hasattr(user, "profile") and user.profile.department:
        qs = RepairTag.objects.filter(department=user.profile.department)
    else:
        qs = RepairTag.objects.none()

    # Convert annotated QuerySets to list of dicts for JSON response
    def breakdown(queryset, field):
        return list(queryset.values(field).annotate(count=Count('id')))

    stats = {
        "total_tags": qs.count(),
        "status_breakdown": breakdown(qs, 'status'),
        "priority_breakdown": breakdown(qs, 'priority'),
        "repair_type_breakdown": breakdown(qs, 'repair_type'),
    }

    return Response(stats)