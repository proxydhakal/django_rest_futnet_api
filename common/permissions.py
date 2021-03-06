from rest_framework import permissions
from apis.accounts.models import User

class IsAdminOrUser(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            return str(request.user.role) in [role for role, name in User.ROLES if name in ['Admin','User']]
        except Exception as e:
            return False

class IsAdminOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            return str(request.user.role) in [role for role, name in User.ROLES if name in ['Admin']]
        except Exception as e:
            return False




class UserIsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS or obj.id == request.user.id