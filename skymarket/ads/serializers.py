from typing import Tuple

from django.db.models import Model
from rest_framework import serializers

from ads.models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    The CommentSerializer class inherits from the serializer class.ModelSerializer is a class for convenient
    serialization and deserialization of objects of the Comment class.
    """
    author_id = serializers.ReadOnlyField(source="author.id", required=False, read_only=True)
    author_first_name = serializers.ReadOnlyField(source="author.first_name", read_only=True)
    author_last_name = serializers.ReadOnlyField(source="author.last_name", read_only=True)
    ad_id = serializers.ReadOnlyField(source="ad.id", required=False, read_only=True)

    class Meta:
        """
        The Meta class is an internal service class of the serializer,
        defines the necessary parameters for the serializer to function.
        """
        model: Model = Comment
        fields: Tuple[str] = ("pk", "author_first_name", "author_last_name", "ad_id", "author_id", "author",
                              "ad", "text", "created_at",)


class AdSerializer(serializers.ModelSerializer):
    """
    The AdSerializer class inherits from the serializer class.ModelSerializer is a class for convenient
    serialization and deserialization of objects of the Ad class.
    """
    author_id = serializers.ReadOnlyField(source="author.id", read_only=True, required=False)
    author_first_name = serializers.ReadOnlyField(source="author.first_name", read_only=True, required=False)
    author_last_name = serializers.ReadOnlyField(source="author.last_name", read_only=True, required=False)

    class Meta:
        """
        The Meta class is an internal service class of the serializer,
        defines the necessary parameters for the serializer to function.
        """
        model: Model = Ad
        fields: Tuple[str] = ("pk", "title", "author_id", "created_at", "description",
            "price", "image", "author_first_name", "author_last_name", "author")
