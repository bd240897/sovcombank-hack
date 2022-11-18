from django.db import models
from django.contrib.auth.models import User
import requests as requests_lib
from django.urls import reverse


class Profile(models.Model):
    """Дополнительные данные для профиля юзера"""
    first_name = models.CharField(max_length=100, blank=True, null=True)
    second_name = models.CharField(max_length=100, blank=True, null=True)
    third_name = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(upload_to='bank/profile', default='bank/profile/avatar_default.png')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_user', db_index=True)
    active = models.BooleanField(default=True)


class Currency(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    active = models.BooleanField(default=True)


class CurrencyCourse(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='currency')
    course_cb = models.FloatField(blank=True, default=0)
    date = models.DateField(db_index=True)


class Account(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile_user', db_index=True)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='currency')
    value = models.FloatField(blank=True, default=0)
    active = models.BooleanField(default=True)


class Transfer(models.Model):
    from_account = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='from_account')
    to_account = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='to_account')
    value = models.FloatField(blank=True, default=0)
    date = models.DateTimeField()
