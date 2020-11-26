from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class BaseProductPagination(PageNumberPagination):
    page = 1 
    page_size_query_param = 'page'
    max_page_size = 100000

    def get_paginated_response(self, data):
        return Response({
            'all_counts': self.page.paginator.count,
            'products': data
        })