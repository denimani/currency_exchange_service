from rest_framework.generics import ListAPIView, RetrieveAPIView

from currency.models import Currency
from currency.paginators import CurrencyPaginator
from currency.serializers import CurrencySerializer


class CurrencyListView(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = CurrencyPaginator


class CurrencyRetrieveView(RetrieveAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
