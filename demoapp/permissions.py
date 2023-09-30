# artist/permissions.py

from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to perform actions on it.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the user is the owner of the object
        return obj.user == request.user
