from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    """
    The UserRegistrationSerializer class inherits from the UserCreateSerializer class from djoser.serializers.
    This is a class for convenient serialization and deserialization of objects of the User class when processing
    create new instance of User class.
    """
    class Meta(BaseUserRegistrationSerializer.Meta):
        """
        The Meta class is an internal service class of the serializer,
        defines the necessary parameters for the serializer to function.
        """
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'phone', 'image')


class CurrentUserSerializer(serializers.ModelSerializer):
    """
    The CurrentUserSerializer class inherits from the ModelSerializer class from rest_framework.serializers module.
    This is a class for convenient serialization and deserialization of objects of the User class when processing
    action with instance of User class.
    """
    class Meta(BaseUserRegistrationSerializer.Meta):
        """
        The Meta class is an internal service class of the serializer,
        defines the necessary parameters for the serializer to function.
        """
        model = User
        fields = ('first_name', 'last_name', 'phone', 'image')
