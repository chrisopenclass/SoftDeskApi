from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    message = "pAccess Denied You don't have permission to access"

    def has_object_permission(self, request, view,  obj):

        if obj.author == request.user:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
