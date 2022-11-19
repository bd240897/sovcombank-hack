import os.path
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework import viewsets, status, generics, pagination, filters, permissions
from rest_framework.views import APIView
import urllib.parse
from PIL import Image
from .models import Profile, Currency, CurrencyCourse, Wallet, Transfer
from .models import Data
from .serializers import DataSerialiser
from django.conf import settings


class ProfileView(generics.GenericAPIView):
    """Профиль"""

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """Отправка ссылки на файл (необработанный)"""
        current_user = request.user
        current_profile = Profile.objects.get(user=current_user)
        if current_profile.active:
            example = {
                "first_name": current_profile.first_name,
                "second_name": current_profile.second_name,
                "last_name": current_profile.third_name,
                "avatar": current_profile.avatar,
                'active': True
            }
        else:
            example = {
                'active': False
            }
        return Response(example, status=status.HTTP_200_OK)


class DataListView(generics.ListAPIView):
    """Получение списка тегов"""

    queryset = Data.objects.all()
    serializer_class = DataSerialiser
    permission_classes = [permissions.AllowAny]


# class WalletView(generics.GenericAPIView):
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


class WalletListView(generics.GenericAPIView):
    """Список кошельков"""

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """Отправка ссылки на файл (необработанный)"""
        current_user = request.user
        wallets = Wallet.objects.filter(owner=Profile.objects.get(user=current_user))
        wallets_list = [{'id': i, 'name': wallets[i].name, 'currency': wallets[i].currency.name,
                         'value': wallets[i].value} for i in range(len(wallets))]
        example = {"list": wallets_list}

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
