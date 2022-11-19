from django.urls import path, include
from .views import DataDetailView, DataListView, ProfileView, WalletView, TransferCoinView, WalletListView

urlpatterns = [path("data/", DataDetailView.as_view()),
               path("data/list/", DataListView.as_view()),

                path("profile/", ProfileView.as_view()),
                path("wallet/", WalletView.as_view()),
                path("wallet/list/", WalletListView.as_view()),
                path("transfer/", TransferCoinView.as_view()),
               ]
