from rest_framework import permissions
'''
Custom permissions for users to edit their own user
'''
class UserPermisions(permissions.BasePermission):
    def has_permission(self, request, view):
        return True
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if not request.user.is_anonymous:
            return request.user == obj
        return False
'''Permissions to allow users to only edit thier profile'''    
class IsProfileOwnweOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):

        return True
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_anonymous:
            return request.user.profile == obj
        return False
    

class IsSuperUserOrReadOnly(permissions.BasePermission):
    """
    Superuser can edit any profile; others can only read.
    """
    def has_permission(self, request, view):
        # Everyone can read
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only superuser can write
        return request.user and request.user.is_superuser