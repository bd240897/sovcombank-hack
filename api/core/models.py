from django.db import models
from django.contrib.auth.models import User
import requests as requests_lib
from django.utils.timezone import now

from django.urls import reverse


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
    """Дополнительные данные для профиля юзера"""
    first_name = models.CharField(max_length=100, blank=True, null=True)
    second_name = models.CharField(max_length=100, blank=True, null=True)
    third_name = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(upload_to='core/profile', default='core/profile/avatar_default.png')
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='profile_user', db_index=True)
    active = models.BooleanField(default=True)
    date_creation = models.DateTimeField(default=now, editable=False)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return str(', '.join((str(self.first_name), str(self.second_name), str(self.third_name))))


class Currency(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    code = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'

    def __str__(self):
        return str(self.name)


class CurrencyCourse(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='currency_course_currency')
    course_cb = models.FloatField(blank=True, default=0)
    date = models.DateField(default=now, editable=False)

    class Meta:
        verbose_name = 'Курс валюты'
        verbose_name_plural = 'Курсы валюты'

    def __str__(self):
        return str(', '.join((str(self.currency.name), str(self.date))))


class Wallet(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='wallet_owner', db_index=True)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='wallet_currency')
    value = models.FloatField(blank=True, default=0)
    active = models.BooleanField(default=True)
    date_creation = models.DateTimeField(default=now, editable=False)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Кошелек'
        verbose_name_plural = 'Кошельки'

    def __str__(self):
        return str((', '.join((str(self.owner), str(self.name)))))


class Transfer(models.Model):
    from_account = models.ForeignKey(Wallet, on_delete=models.PROTECT, related_name='transfers_from_account')
    to_account = models.ForeignKey(Wallet, on_delete=models.PROTECT, related_name='transfers_to_account')
    value = models.FloatField(blank=True, default=0)
    # currency = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='transfer_currency')
    date = models.DateTimeField(default=now, editable=False)

    class Meta:
        verbose_name = 'Перевод'
        verbose_name_plural = 'Переводы'

    def __str__(self):
        return str(', '.join((str(self.from_account_id), str(self.to_account_id), str(self.date))))
