from django.db import models
from django.contrib.auth.models import User
import requests as requests_lib
from django.urls import reverse
from django.utils.timezone import now

class Data(models.Model):
    """Комментарии"""
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    img = models.ImageField(upload_to="core/")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='data_user', default=1)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class Profile(models.Model):
    """Профиль юзера"""

    first_name = models.CharField(verbose_name="Имя", max_length=100, blank=True, null=True)
    second_name = models.CharField(verbose_name="Фамилия", max_length=100, blank=True, null=True)
    third_name = models.CharField(verbose_name="Отчество", max_length=100, blank=True, null=True)
    avatar = models.ImageField(verbose_name="Аватарка", upload_to='core/profile', default='core/profile/avatar_default.png')
    user = models.OneToOneField(User, verbose_name="Юзер", on_delete=models.CASCADE, related_name='profile_user', db_index=True)
    active = models.BooleanField(verbose_name="Статус", default=True)
    date_creation = models.DateTimeField(verbose_name="Дата создания", default=now, editable=False)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Currency(models.Model):
    """Валюта"""

    name = models.CharField(verbose_name="Название", max_length=100)
    country = models.CharField(verbose_name="Страна", max_length=100)
    active = models.BooleanField(verbose_name="Статус", default=True)

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'


class CurrencyCourse(models.Model):
    """Курс валюты"""

    currency = models.ForeignKey(Currency, verbose_name="Валюта", on_delete=models.CASCADE, related_name='currency_course_currency')
    course_cb = models.FloatField(verbose_name="Курс валюты", blank=True, default=0)
    # TODO for what?
    date = models.DateField(verbose_name="Дата", default=now, editable=False)

    class Meta:
        verbose_name = 'Курс валюты'
        verbose_name_plural = 'Курсы валюты'


class Wallet(models.Model):
    """Кошелек"""

    owner = models.ForeignKey(User, verbose_name="Владелец", on_delete=models.CASCADE, related_name='wallet_owner', db_index=True)
    currency = models.ForeignKey(Currency, verbose_name="Валюта", on_delete=models.PROTECT, related_name='wallet_currency')
    value = models.FloatField(verbose_name="Количество", blank=True, default=0)
    active = models.BooleanField(verbose_name="Статус", default=True)
    date_creation = models.DateTimeField(verbose_name="Дата", default=now, editable=False)

    class Meta:
        verbose_name = 'Кошелек'
        verbose_name_plural = 'Кошельки'


class Transfer(models.Model):
    """История переводов"""

    from_account = models.ForeignKey(Wallet, verbose_name="От какого кошелька", on_delete=models.PROTECT, related_name='transfers_from_account')
    to_account = models.ForeignKey(Wallet, verbose_name="В какой кошелек", on_delete=models.PROTECT, related_name='transfers_to_account')
    value = models.FloatField(verbose_name="Количество", blank=True, default=0)
    currency = models.ForeignKey(Currency, verbose_name="Валюта", on_delete=models.PROTECT, related_name='transfer_currency')
    date = models.DateTimeField(verbose_name="Дата", default=now, editable=False)

    class Meta:
        verbose_name = 'Перевод'
        verbose_name_plural = 'Переводы'
