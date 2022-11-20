import os.path

from django.http import QueryDict
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser, JSONParser
from rest_framework import viewsets, status, generics, pagination, filters, permissions
from rest_framework.views import APIView
import urllib.parse
from PIL import Image
from .models import Data, Profile, Wallet, Transfer
from .serializers import DataSerialiser, WalletSerialiser, ProfileSerialiser, TransferSerialiser, WalletListSerialiser
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

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """Отправка ссылки на файл (необработанный)"""

        current_user = request.user
        current_profile = Profile.objects.get(user=current_user)
        serializer = ProfileSerialiser(current_profile)
        print(serializer.data)

        # example = {
        #     "first_name": "Дмитрий",
        #     "second_name": "Алексеевич",
        #     "last_name": "Борисов",
        #     "avatar": "https://pixelbox.ru/wp-content/uploads/2021/02/mult-ava-instagram-69.jpg",
        #     'active': True
        # }

        return Response(serializer.data, status=status.HTTP_200_OK)


class WalletView(generics.GenericAPIView):
    """Данные по кошельку (счет)"""

    permission_classes = [permissions.IsAuthenticated]

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
        # return Response(example, status=status.HTTP_200_OK)
        current_user = request.user
        wallet = Wallet.objects.get(owner=current_user, id=id)
        serializer = WalletSerialiser(wallet)
        return Response(serializer.data)

class WalletListView(generics.GenericAPIView):
    """Список кошельков"""

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """Отправка ссылки на файл (необработанный)"""

        # example = {"list": [
        #     {
        #         "id": 1,
        #         "name": "Кошка-жена",
        #         "currency": "USD",  #
        #         "value": 10000,
        #     },
        #     {
        #         "id": 2,
        #         "name": "Зарплата",
        #         "currency": "EUR",  #
        #         "value": 100,
        #     }]
        # }

        current_user = request.user
        wallet = Wallet.objects.filter(owner=current_user)
        serializer = WalletListSerialiser(wallet, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class TransferCoinView(generics.GenericAPIView):
    """Перевод денег"""

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        """Отправка ссылки на файл (необработанный)"""

        # example = {
        #     "from_account": 1,  # id
        #     "to_account": 2,  # id
        #     "value": 50,
        #     "currency": "USD"
        # }

        # https://stackoverflow.com/questions/33861545/how-can-modify-request-data-in-django-rest-framework
        # добавим пользователя в список request.data - тут он требует добавлять id а не юзер

        if isinstance(request.data, QueryDict):  # optional
            request.data._mutable = True
        current_user = request.user
        request.data.update({"owner": current_user.id})

        serializer = TransferSerialiser(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class TransferHistoryView(generics.GenericAPIView):
    """Перевод денег"""

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """Отправка ссылки на файл (необработанный)"""

        # id = request.POST.get('id')  # id
        #
        # example = {
        #     "date": "10-10-10:21:21",
        #     "from_account_id": 1,  # id
        #     "to_account_id": 2,  # id
        #     "from_account_name": "Зарплата",
        #     "to_account_name": "Кошка-жена",
        #     "value": 50,
        # }

        current_user = request.user
        transfers = Transfer.objects.filter(owner=current_user)
        serializer = TransferSerialiser(transfers, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


# TODO мб не будет использоваться
class GetWalletName(generics.GenericAPIView):
    """Получить имя счета по его id"""

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """Отправка ссылки на файл (необработанный)"""

        id = request.query_params.get('id') # id

        example = {
                "id": 1,
                "name": "Зарплата",
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


class CourseHistoryView(generics.GenericAPIView):
    """История курса"""

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """Отправка ссылки на файл (необработанный)"""

        name = request.query_params.get('name') # имя валюты

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


