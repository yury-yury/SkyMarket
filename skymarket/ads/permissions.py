from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """
    The IsAdmin class inherits from the BasePermission class from the permissions module
    of the rest_framework library. Controls access to protected endpoints.
    Allows access only to authenticated users with the administrator role.
    """
    message: str = "You must have role ADMIN"

    def has_permission(self, request, view) -> bool:
        """
        The has_permission function overrides the method of the base class. Accepts as arguments
        a request object and a view object. Checks the user's access rights to the requested actions.
        Returns True if the test result is positive, otherwise False.
        """
        return request.user.role == "admin"



class IsExecutor(BasePermission):
    """
    The IsExecutor class inherits from the BasePermission class from the permissions module
    of the rest_framework library. Controls access to protected endpoints.
    Allows access only to authenticated users who are the owners of the records.
    """
    message: str = "You must be the owner of the record."

    def has_object_permission(self, request, view, obj) -> bool:
        """
        The has_object_permission function overrides the method of the base class. Accepts as arguments
        a request object, a view object, and a database object requested for editing.
        Checks the user's access rights to the requested actions. Returns True if the test result
        is positive, otherwise False.
        """
        return obj.author == request.user
