from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUserOrStaffReadOnly(BasePermission):
    """
    Custom permission for Serialized data.when this permission
    added to the class view, only superusers can edit the data, others just can only see
    the data.
    """

    def has_permission(self, request, view) -> bool:
        return bool(
            request.method in SAFE_METHODS and request.user.is_authenticated and request.user.is_staff
            or request.user.is_authenticated and request.user.is_superuser)
