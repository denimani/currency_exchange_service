from rest_framework.pagination import PageNumberPagination


class CurrencyPaginator(PageNumberPagination):
    page_size = 10
