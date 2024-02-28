from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название валюты')
    rate = models.DecimalField(max_digits=10, decimal_places=4, verbose_name='Курс валюты к рублю')

    def __str__(self):
        return f'Валюта - {self.name}'

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'
