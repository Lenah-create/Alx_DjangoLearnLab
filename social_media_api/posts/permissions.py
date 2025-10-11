from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission: only the author can edit/delete; others read-only.
    """

    def has_object_permission(self, request, view, obj):
        # Read-only for safe methods
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only for the author
        return obj.author == request.user
