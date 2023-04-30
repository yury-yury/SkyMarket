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
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = AdPagination
    filter_backends = (DjangoFilterBackend, )
    filterset_class = AdFilter

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = [AllowAny,]
        elif self.action == "retrieve":
            self.permission_classes = [IsAuthenticated, ]
        else:
            self.permission_classes = [IsAuthenticated, IsAdmin | IsExecutor]

        return super().get_permissions()

    @action(detail=False, methods=['get'])
    def me(self, request, *args, **kwargs):
        self.queryset = Ad.objects.filter(author=request.user)
        return super().list(self, request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    """ Вьюсет который выводит список всех объектов """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        ad_id = self.kwargs.get("ads_pk")
        ad_instance = get_object_or_404(Ad, id=ad_id)
        user = self.request.user
        serializer.save(author=user, ad=ad_instance)

    def get_queryset(self, *args, **kwargs):
        comment = self.kwargs.get('ads_pk')
        return super().get_queryset().filter(ad=comment)

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = [AllowAny, ]
        elif self.action == "retrieve":
            self.permission_classes = [IsAuthenticated, ]
        else:
            self.permission_classes = [IsAuthenticated, IsAdmin | IsExecutor, ]
        return super().get_permissions()

