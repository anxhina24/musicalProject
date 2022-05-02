from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet

from musicApp.models import Works
from musicApp.serializers import WorksSerializer


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class QueryWorksViewSet(GenericViewSet, mixins.ListModelMixin):
    serializer_class = WorksSerializer
    pagination_class = LargeResultsSetPagination
    def get_queryset(self):
        query_var = self.request.query_params['worksList'].split(',')
        queryset = Works.objects.filter(iswc__in=query_var)
        return queryset
