from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Data, Transfer, Wallet, CurrencyCourse, Currency, Profile


class DataSerialiser(serializers.ModelSerializer):
    """Загруженные данные"""

    img = serializers.SerializerMethodField()
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Data
        fields = ('id', 'time', 'name',  'user', 'description', 'img',)

    def get_img(self, model):
        request = self.context.get('request')
        img = model.img.url
        return request.build_absolute_uri(img)


class ProfileSerialiser(serializers.ModelSerializer):
    """Загруженные данные"""

    class Meta:
        model = Profile
        fields = ('id', 'first_name', 'second_name', 'third_name', 'avatar', 'active', 'date_creation',)


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

    currency = serializers.SerializerMethodField()

    class Meta:
        model = Wallet
        fields = "__all__"

    def get_currency(self, obj):
        return obj.currency.name

class WalletListSerialiser(serializers.ModelSerializer):
    """Загруженные данные"""

    currency = serializers.SerializerMethodField()

    class Meta:
        model = Wallet
        fields = ('id', 'name', 'currency', 'value')

    def get_currency(self, obj):
        return obj.currency.name


class TransferSerialiser(serializers.ModelSerializer):
    """Загруженные данные"""

    class Meta:
        model = Transfer
        fields = ('from_account', 'to_account', "value", 'owner')




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