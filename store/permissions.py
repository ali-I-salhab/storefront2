from rest_framework.permissions import BasePermission,IsAdminUser


SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
class IsAdminUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return   bool(request.method in SAFE_METHODS or
           request.user and request.user.is_staff)