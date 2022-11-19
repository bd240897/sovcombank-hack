import os.path
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework import viewsets, status, generics, pagination, filters, permissions
from rest_framework.views import APIView
import urllib.parse
from PIL import Image
from .models import Data
from .serializers import DataSerialiser
from django.conf import settings


class DataDetailView(generics.GenericAPIView):
    """Отправка файлов"""

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """Отправка ссылки на файл (необработанный)"""

        # парсим запрос
        id = request.query_params.get('id')

        # проверки
        if not id:
            return Response(f"You didn't send id", status=status.HTTP_404_NOT_FOUND)
        elif not Data.objects.filter(pk=id).exists():
            return Response(f"File with id = {id} not found!", status=status.HTTP_404_NOT_FOUND)

        request_data = Data.objects.get(pk=id)
        serialized = DataSerialiser(request_data, context={"request": request})
        return Response(serialized.data, status=status.HTTP_200_OK)


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

        example = {
            "first_name": "Дмитрий",
            "second_name": "Дмитрий",
            "last_name": "Дмитрий",
            "avatar": "https://pixelbox.ru/wp-content/uploads/2021/02/mult-ava-instagram-69.jpg",
            'active': True
        }

        return Response(example, status=status.HTTP_200_OK)


class WalletView(generics.GenericAPIView):
    """Данные по кошельку"""

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """Отправка ссылки на файл (необработанный)"""

        id = request.GET.get('id')

        print(request.GET)

        example = {
            "owner": "Дмитрий",  # 1
            "currency": "USD",  #
            "value": 10000,
            'active': True
        }

        return Response(example, status=status.HTTP_200_OK)


class WalletListView(generics.GenericAPIView):
    """Список кошельков"""

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """Отправка ссылки на файл (необработанный)"""

        example = {"list": [
            {
                "owner": "Дмитрий",  # 1
                "currency": "USD",  #
                "value": 10000,
                'active': True
            },
            {
                "owner": "Дмитрий",  # 1
                "currency": "EUR",  #
                "value": 100,
                'active': True
            }]
        }

        return Response(example, status=status.HTTP_200_OK)


class TransferCoinView(generics.GenericAPIView):
    """Перевод денег"""

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """Отправка ссылки на файл (необработанный)"""

        from_account = request.DATA.get('from_account')  # id
        to_account = request.DATA.get('to_account')  # id
        value = request.DATA.get('value')
        currency = request.DATA.get('id')  # id

        print(request.DATA)

        example = {
            "from_account": 1,  # id
            "to_account": 2,  # id
            "value": 50,
        }

        return Response(example, status=status.HTTP_200_OK)
