from rest_framework import viewsets, permissions
from .models import RepairTag
from .serializers import RepairTagSerializer
from users.models import Profile


class RepairTagViewSet(viewsets.ModelViewSet):
    queryset = RepairTag.objects.all().order_by('-created_at')
    serializer_class = RepairTagSerializer
    permission_classes = [permissions.IsAuthenticated]
    

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