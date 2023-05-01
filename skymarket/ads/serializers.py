from rest_framework import serializers

from ads.models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    The CommentSerializer class inherits from the serializer class.ModelSerializer is a class for convenient
    serialization and deserialization of objects of the Comment class.
    """
    class Meta:
        """
        The Meta class is an internal service class of the serializer,
        defines the necessary parameters for the serializer to function.
        """
        model = Comment
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    """
    The AdSerializer class inherits from the serializer class.ModelSerializer is a class for convenient
    serialization and deserialization of objects of the Ad class.
    """
    class Meta:
        """
        The Meta class is an internal service class of the serializer,
        defines the necessary parameters for the serializer to function.
        """
        model = Ad
        fields = '__all__'
