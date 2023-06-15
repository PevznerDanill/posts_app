from django.http import HttpRequest
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.views import View


class IsAdminOrReadOnly(BasePermission):
    """
    Checks if the user is the admin, in which case makes unsafe methods
    available. Otherwise, allows only safe methods.
    """
    def has_permission(self, request: HttpRequest, view: View):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_superuser
