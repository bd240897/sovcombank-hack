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
            "second_name": "Алексеевич",
            "last_name": "Борисов",
            "avatar": "https://pixelbox.ru/wp-content/uploads/2021/02/mult-ava-instagram-69.jpg",
            'active': True
        }

        return Response(example, status=status.HTTP_200_OK)


class WalletView(generics.GenericAPIView):
    """Данные по кошельку (счет)"""

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """Отправка ссылки на файл (необработанный)"""

        id = request.GET.get('id')

        print(request.GET)

        example = {
            "id": 1,
            "name": "Кошка-жена",
            "owner": "Дмитрий",  # 1
            "currency": "USD",  #
            "value": 10000,
            "value_in_ruble": 600000,
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
                "id": 1,
                "name": "Кошка-жена",
                "currency": "USD",  #
                "value": 10000,
            },
            {
                "id": 2,
                "name": "Игорь",
                "currency": "EUR",  #
                "value": 100,
            }]
        }

        return Response(example, status=status.HTTP_200_OK)


class TransferCoinView(generics.GenericAPIView):
    """Перевод денег"""

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """Отправка ссылки на файл (необработанный)"""

        from_account = request.POST.get('from_account')  # id
        to_account = request.POST.get('to_account')  # id
        value = request.POST.get('value')
        currency = request.POST.get('id')  # id

        print(request.POST)

        example = {
            "from_account": 1,  # id
            "to_account": 2,  # id
            "value": 50,
        }

        return Response(example, status=status.HTTP_200_OK)


class TransferHistoryView(generics.GenericAPIView):
    """Перевод денег"""

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """Отправка ссылки на файл (необработанный)"""

        id = request.POST.get('id')  # id

        print(request.POST)

        example = {
            "date": "10-10-10:21:21",
            "from_account_id": 1,  # id
            "to_account_id": 2,  # id
            "from_account_name": "Зарплата",  # id
            "to_account_name": "Кошка-жена",  # id
            "value": 50,
        }

        return Response(example, status=status.HTTP_200_OK)


class CourseView(generics.GenericAPIView):
    """Список кошельков"""

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """Отправка ссылки на файл (необработанный)"""

        name = request.query_params.get('name') # имя валюты

        example = {"list": [
            {
                "name": "USD",
                "price": "60",  # в рублях
                "type": "Продать",
            },
            {
                "name": "USD",
                "price": "70",  # в рублях
                "type": "Купить",
            }]
        }

        return Response(example, status=status.HTTP_200_OK)