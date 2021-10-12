from rest_framework.pagination import PageNumberPagination


class ReviewPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'p'
    max_page_size = 50
