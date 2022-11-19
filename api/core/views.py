import os.path
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser, JSONParser
from rest_framework import viewsets, status, generics, pagination, filters, permissions
from rest_framework.views import APIView
import urllib.parse
from PIL import Image
from .models import Profile, Currency, CurrencyCourse, Wallet, Transfer
from .models import Data
from .serializers import DataSerialiser, ProfileSerialiser, Currency, CurrencyCourse, WalletSerialiser, \
    TransferSerialiser, FullTransferSerialiser
from django.conf import settings
from django.db.models import Q
from .currency import get_currency, convert_currency
import json


class DataListView(generics.ListAPIView):
    """Получение списка тегов"""

    queryset = Data.objects.all()
    serializer_class = DataSerialiser
    permission_classes = [permissions.AllowAny]


class ProfileView(generics.GenericAPIView):
    """Профиль"""

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """Отправка ссылки на файл (необработанный)"""
        # current_user = request.user
        id = request.GET.get('id')
        current_profile = Profile.objects.get(user=id)
        # if current_profile.active:
        #     example = {
        #         "first_name": current_profile.first_name,
        #         "second_name": current_profile.second_name,
        #         "last_name": current_profile.third_name,
        #         "avatar": current_profile.avatar,
        #         'active': True
        #     }
        # else:
        #     example = {
        #         'active': False
        #     }
        # return Response(example, status=status.HTTP_200_OK)
        serializer = ProfileSerialiser(current_profile)
        return Response(serializer.data)


# class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Profile.objects.get()
#     serializer_class = P


class WalletView(generics.GenericAPIView):
    """Кошелек"""

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """Отправка ссылки на файл (необработанный)"""

        id = request.GET.get('id')

        wallet = Wallet.objects.get(id=id)
        serializer = WalletSerialiser(wallet)
        return Response(serializer.data)


class WalletListView(generics.GenericAPIView):
    """Список кошельков"""

    permission_classes = [permissions.AllowAny]

    #
    # def get(self, request):
    #     """Отправка ссылки на файл (необработанный)"""
    #     current_user = request.user
    #     wallets = Wallet.objects.filter(owner=Profile.objects.get(user=current_user))
    #     wallets_list = [{'id': i, 'name': wallets[i].name, 'currency': wallets[i].currency.name,
    #                      'value': wallets[i].value} for i in range(len(wallets))]
    #     example = {"list": wallets_list}
    #
    #     return Response(example, status=status.HTTP_200_OK)

    def get(self, request):
        """Отправка ссылки на файл (необработанный)"""

        id = request.GET.get('id')
        # current_user = request.user
        # current_profile = Profile.objects.get(user_id=id)
        wallet = Wallet.objects.filter(owner__in=id)
        serializer = WalletSerialiser(wallet, many=True)
        return Response(serializer.data)


class TransferCoinView(generics.GenericAPIView):
    """Перевод денег"""

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """Отправка ссылки на файл (необработанный)"""

        data = JSONParser().parse(request)
        serializer = TransferSerialiser(data=data)

        # from_account = request.POST.get('from_account')  # id
        # to_account = request.POST.get('to_account')  # id
        # value = request.POST.get('value')
        # currency = request.POST.get('id')  # id

        # проверка на наличии денег и активность аккаунтов

        # print(request.POST)
        if serializer.is_valid():
            print(serializer.validated_data.get('from_account').id)
            print(Wallet.objects.get(id=serializer.validated_data.get('from_account').id).value)
            if Wallet.objects.get(id=serializer.validated_data.get('from_account').id).value >= serializer.validated_data.get('value'):
                wallet_from = Wallet.objects.get(id=serializer.validated_data.get('from_account').id)
                wallet_to = Wallet.objects.get(id=serializer.validated_data.get('to_account').id)
                if wallet_from.currency == wallet_to.currency:
                    wallet_from.value -= serializer.validated_data.get('value')
                    wallet_from.value += serializer.validated_data.get('value')

                else:
                    result = convert_currency(wallet_from.currency.code,
                                              serializer.validated_data.get('value'),
                                              wallet_to.currency.code)
                    wallet_from.value -= serializer.validated_data.get('value')
                    wallet_to.value += result

                wallet_from.save()
                wallet_to.save()
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=400)
        # example = {
        #     "from_account": 1,  # id
        #     "to_account": 2,  # id
        #     "value": 50,
        #     "currency": "USD"
        # }
        #
        # return Response(example, status=status.HTTP_200_OK)


class TransferHistoryView(generics.GenericAPIView):
    """Перевод денег"""

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """Отправка ссылки на файл (необработанный)"""

        id = request.GET.get('id') # id

        transfers = Transfer.objects.filter(Q(from_account_id=id) | Q(to_account_id=id))
        serializer = TransferSerialiser(transfers, many=True)

        return Response(serializer.data)


# TODO мб не будет использоваться
class GetWalletName(generics.GenericAPIView):
    """Получить имя счета по его id"""

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """Отправка ссылки на файл (необработанный)"""

        id = request.query_params.get('id')  # id

        example = {
            "id": id,
            "name": Wallet.objects.get(id=id).name,
        }

        return Response(example, status=status.HTTP_200_OK)


class CourseView(generics.GenericAPIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """Отправка ссылки на файл (необработанный)"""

        name_from = request.query_params.get('name_from')  # имя валюты
        name_to = request.query_params.get('name_to')  # имя валюты
        name_from = Currency.objects.get(name=name_from).code
        name_to = Currency.objects.get(name=name_to).code
        result = get_currency(name_from, name_to)
        # print(json.loads(result)['rates'][name_from])
        return Response(result, status=status.HTTP_200_OK)


class CourseHistoryView(generics.GenericAPIView):
    """История курса"""

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """Отправка ссылки на файл (необработанный)"""

        name = request.query_params.get('name')  # имя валюты

        # TODO
        example = {"list": [
            {
                "1": "1",
            },
            {
                "2": "2",
            }]
        }

        return Response(example, status=status.HTTP_200_OK)

# class TransferView(generics.GenericAPIView):
#     """Кошелек"""
#
#     permission_classes = [permissions.AllowAny]
#
#     def get(self, request):
#         """Отправка ссылки на файл (необработанный)"""
#         current_user = request.user
#         current_profile = Profile.objects.get(user=current_user)
#         if current_profile.active:
#             example = {
#                 "first_name": current_profile.first_name,
#                 "second_name": current_profile.second_name,
#                 "last_name": current_profile.third_name,
#                 "avatar": current_profile.avatar,
#                 'active': True
#             }
#         else:
#             example = {
#                 'active': False
#             }
#         return Response(example, status=status.HTTP_200_OK)


# class TransferListView(generics.GenericAPIView):
#     """Список кошельков"""
#
#     permission_classes = [permissions.AllowAny]
#
#     def get(self, request):
#         """Отправка ссылки на файл (необработанный)"""
#         current_user = request.user
#         wallets = Wallet.objects.filter(owner=Profile.objects.get(user=current_user))
#         wallets_list = [{'id': i, 'name': wallets[i].name, 'currency': wallets[i].currency.name,
#                          'value': wallets[i].value} for i in range(len(wallets))]
#         example = {"list": wallets_list}
#
#         return Response(example, status=status.HTTP_200_OK)


# class CurrencyCourseView(generics.GenericAPIView):
#     """Кошелек"""
#
#     permission_classes = [permissions.AllowAny]
#
#     def get(self, request):
#         """Отправка ссылки на файл (необработанный)"""
#         current_user = request.user
#         current_profile = Profile.objects.get(user=current_user)
#         if current_profile.active:
#             example = {
#                 "first_name": current_profile.first_name,
#                 "second_name": current_profile.second_name,
#                 "last_name": current_profile.third_name,
#                 "avatar": current_profile.avatar,
#                 'active': True
#             }
#         else:
#             example = {
#                 'active': False
#             }
#         return Response(example, status=status.HTTP_200_OK)


# class CurrencyCourseListView(generics.GenericAPIView):
#     """Список кошельков"""
#
#     permission_classes = [permissions.AllowAny]
#
#     def get(self, request):
#         """Отправка ссылки на файл (необработанный)"""
#         current_user = request.user
#         wallets = Wallet.objects.filter(owner=Profile.objects.get(user=current_user))
#         wallets_list = [{'id': i, 'name': wallets[i].name, 'currency': wallets[i].currency.name,
#                          'value': wallets[i].value} for i in range(len(wallets))]
#         example = {"list": wallets_list}
#
#         return Response(example, status=status.HTTP_200_OK)
