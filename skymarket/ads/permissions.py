# TODO здесь производится настройка пермишенов для нашего проекта
from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    message = "You must have role ADMIN"

    def has_permission(self, request, view):
        if request.user.role == "admin":
            return True
        return False


class IsExecutor(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
