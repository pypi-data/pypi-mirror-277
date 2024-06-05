"""Application logic for rendering HTML templates and handling HTTP requests.

View objects handle the processing of incoming HTTP requests and return the
appropriately rendered HTML template or other HTTP response.
"""

from rest_framework import permissions, viewsets

from .models import *
from .permissions import StaffWriteAuthenticatedRead
from .serializers import *

__all__ = [
    'ResearchGroupViewSet',
    'UserViewSet',
]


class ResearchGroupViewSet(viewsets.ModelViewSet):
    """Manage user membership in research groups"""

    queryset = ResearchGroup.objects.all()
    permission_classes = [permissions.IsAuthenticated, StaffWriteAuthenticatedRead]
    serializer_class = ResearchGroupSerializer

    def get_queryset(self) -> list[ResearchGroup]:
        """Return a list of all research groups to admins, or the requesting users research groups"""

        if self.request.user.is_staff:
            return self.queryset

        return ResearchGroup.objects.groups_for_user(self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    """Read only access to user data"""

    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, StaffWriteAuthenticatedRead]
    serializer_class = UserSerializer
