from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Data
from .models import Profile, Currency, CurrencyCourse, Wallet, Transfer


class DataSerialiser(serializers.ModelSerializer):
    """Загруженные данные"""

    img = serializers.SerializerMethodField()
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Data
        fields = ('id', 'time', 'name', 'user', 'description', 'img',)

    def get_img(self, model):
        request = self.context.get('request')
        img = model.img.url
        return request.build_absolute_uri(img)


class ProfileSerialiser(serializers.ModelSerializer):
    """Загруженные данные"""

    class Meta:
        model = Profile
        fields = ('id', 'first_name', 'second_name', 'last_name', 'avatar', 'active', 'date_creation',)


class CurrencySerialiser(serializers.ModelSerializer):
    """Загруженные данные"""

    class Meta:
        model = Currency
        fields = ('id', 'name', 'country',)


class CurrencyCourseSerialiser(serializers.ModelSerializer):
    """Загруженные данные"""

    currency = serializers.SerializerMethodField()

    class Meta:
        model = CurrencyCourse
        fields = ('id', 'first_name', 'course_cb', 'date', 'currency',)

    def get_currency(self, obj):
        return obj.currency.name


class WalletSerialiser(serializers.ModelSerializer):
    """Загруженные данные"""
    owner_first_name = serializers.SerializerMethodField()
    owner_second_name = serializers.SerializerMethodField()
    owner_third_name = serializers.SerializerMethodField()
    currency = serializers.SerializerMethodField()

    class Meta:
        model = Wallet
        fields = ('id', 'currency', 'date_creation', 'value', 'owner_first_name', 'owner_second_name',
                  'owner_third_name', 'name',)

    def get_owner_first_name(self, obj):
        return obj.owner.first_name

    def get_owner_second_name(self, obj):
        return obj.owner.second_name

    def get_owner_third_name(self, obj):
        return obj.owner.third_name

    def get_currency(self, obj):
        return obj.currency.name


class TransferSerialiser(serializers.ModelSerializer):
    """Загруженные данные"""
    from_account_id = serializers.SerializerMethodField()
    to_account_id = serializers.SerializerMethodField()

    class Meta:
        model = Transfer
        fields = ('currency', 'value', 'from_account_id', 'to_account_id',)

    def get_from_account_id(self, obj):
        return obj.from_account.id

    def get_to_account_id(self, obj):
        return obj.to_account.id


class FullTransferSerialiser(TransferSerialiser):
    from_account_name = serializers.SerializerMethodField()
    to_account_name = serializers.SerializerMethodField()
    currency = serializers.SerializerMethodField()

    class Meta:
        model = Transfer
        fields = ('currency', 'value', 'from_account_id', 'to_account_id', 'from_account_name', 'to_account_name',
                  'currency', 'id', 'date')

    def get_from_account_name(self, obj):
        return obj.from_account.name

    def get_to_account_name(self, obj):
        return obj.to_account.name

    def get_currency(self, obj):
        return obj.currency.name