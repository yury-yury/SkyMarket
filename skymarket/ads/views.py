from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated

from ads.models import Ad, Comment
from ads.permissions import IsAdmin, IsExecutor
from ads.serializers import AdSerializer, CommentSerializer
from ads.filters import AdFilter


class AdPagination(pagination.PageNumberPagination):
    """
    The AdPagination class inherits from the PageNumber Pagination class from the pagination library.
    Overrides the pagination rules for individual endpoints.
    """
    page_size: int = 4


class AdViewSet(viewsets.ModelViewSet):
    """
    The AdViewSet class inherits from the ModelViewSet class, which is designed to handle all requests
    determined by CRUD methods to the Ad model. And also extends the methods of the base class.
    """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = AdPagination
    filter_backends = (DjangoFilterBackend, )
    filterset_class = AdFilter

    def create(self, request, *args, **kwargs):
        """
        The create function complements the base class method with additional functionality, autofill
        of the author field with the value of the current user. The function takes as arguments the instance
        of the class itself, the request object, and all other positional and named parameters. After that,
        the method of the parent class is called.
        """
        self.request.data["author"] = self.request.user.id
        return super().create(request, *args, **kwargs)

    def get_permissions(self):
        """
        The get_permissions function is a method of the AdViewSet class and extends the functionality
        of the base class method. Assigns access restrictions to various endpoints included
        in the implemented by this class.
        """
        if self.action == "list":
            self.permission_classes = [AllowAny, ]
        elif self.action in ["retrieve", "me", ]:
            self.permission_classes = [IsAuthenticated, ]
        else:
            self.permission_classes = [IsAuthenticated, IsAdmin | IsExecutor]

        return super().get_permissions()


    @action(detail=False, methods=['get'])
    def me(self, request, *args, **kwargs):
        """
        The me function is a method of the AdViewSet class and extends the CRUD methods of the base class.
        Adds a custom endpoint.
        """
        self.queryset = Ad.objects.filter(author=request.user).all()
        return super().list(self, request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    """
    The CommentViewSet class inherits from the ModelViewSet class, which is designed to handle all requests
    determined by CRUD methods to the Comment model. And also extends the methods of the base class.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        """
        The create function complements the base class method with additional functionality, autofill
        of the author field with the value of the current user and autofill ad field with value of current ad.
        The function takes as arguments the instance of the class itself, the request object, and all other positional
        and named parameters. After that, the method of the parent class is called.
        """
        self.request.data["author"] = self.request.user.id
        self.request.data["ad"] = self.kwargs.get("ads_pk")
        return super().create(request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        """
        The get_queryset function is a utility method of the CommentViewSet class and extends the method
        of the base class. Overrides the queryset used by the class when processing endpoints processed by this class.
        """
        comment = self.kwargs.get('ads_pk')
        return super().get_queryset().filter(ad=comment)

    def get_permissions(self):
        """
        The get_permissions function is a method of the CommentViewSet class and extends the functionality
        of the base class method. Assigns access restrictions to various endpoints included
        in the implemented by this class.
        """
        if self.action == "list":
            self.permission_classes = [AllowAny, ]
        elif self.action == "retrieve":
            self.permission_classes = [IsAuthenticated, ]
        else:
            self.permission_classes = [IsAuthenticated, IsAdmin | IsExecutor, ]
        return super().get_permissions()

