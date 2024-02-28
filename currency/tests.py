from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from currency.models import Currency


class CurrencyTestCase(APITestCase):

    def setUp(self):
        self.maxDiff = None
        self.user = User.objects.create_user(username='admin', email='admin@admin.com', password='12345')
        self.currency_first = Currency.objects.create(
            name='USD',
            rate=99.9912,
        )
        self.currency_second = Currency.objects.create(
            name='EUR',
            rate=100.1212,
        )

    def test_get_currencies_list(self):
        """
        Тест на получение списка валют
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('currency:currencies'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 2)

    def test_get_currency_by_id(self):
        """
        Тест на получение валюты по id
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('currency:currency', kwargs={'pk': self.currency_first.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'USD')
        self.assertEqual(response.data['rate'], '99.9912')
