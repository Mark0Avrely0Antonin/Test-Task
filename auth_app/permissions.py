from rest_framework.permissions import BasePermission
from rest_framework.exceptions import AuthenticationFailed


class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.role == 'AD':
                return True
            return False
        raise AuthenticationFailed
