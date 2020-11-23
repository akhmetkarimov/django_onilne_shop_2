from rest_framework.pagination import PageNumberPagination

class BaseProductPagination(PageNumberPagination):
    page = 1 
    page_size_query_param = 'page'
    max_page_size = 100000