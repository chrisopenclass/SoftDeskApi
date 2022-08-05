from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    message = "Seul un auteur ou contributeur peut effectuer des opérations"

    def has_object_permission(self, request, view,  obj):

        if obj.author == request.user:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
