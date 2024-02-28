import requests
import xml.etree.ElementTree as ET

from django.core.management import BaseCommand

from currency.models import Currency


class Command(BaseCommand):
    """
    Команда для обновления данных валют в БД
    """

    def handle(self, *args, **options):
        url = 'http://www.cbr.ru/scripts/XML_daily.asp'
        response = requests.get(url)
        root = ET.fromstring(response.content)
        for currency in root.findall('Valute'):
            name = currency.find('Name').text
            value = currency.find('Value').text
            Currency.objects.update_or_create(name=name, rate=float(value.replace(',', '.')))
