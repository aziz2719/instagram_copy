from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsPublicationOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsCommentOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        elif request.method == 'DELETE':
            return obj.owner == request.user or obj.publication.owner == request.user
        return obj.owner == request.user