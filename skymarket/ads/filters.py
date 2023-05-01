import django_filters

from ads.models import Ad


class AdFilter(django_filters.rest_framework.FilterSet):
    """
    The AdFilter class inherits from the Filter Set class of the django_filters.rest_framework library
    and configures the search by specifying the search field "title" and its 'icontains' type.
    """
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        """
        A metaclass is an internal service class that defines the necessary parameters for the production of ad search.
        """
        model = Ad
        fields = ('title', )
