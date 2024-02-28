from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from currency.apps import CurrencyConfig
from currency.views import CurrencyListView, CurrencyRetrieveView

app_name = CurrencyConfig.name

urlpatterns = [
    path('currencies/', CurrencyListView.as_view(), name='currencies'),
    path('currency/<int:pk>/', CurrencyRetrieveView.as_view(), name='currency'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
