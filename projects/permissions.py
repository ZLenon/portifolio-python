from rest_framework.permissions import IsAuthenticated as isa


class IsOwnerOrSuperuser(isa):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or obj.user == request.user
