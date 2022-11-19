from django.urls import path, include
from .views import DataListView
from .views import ProfileView, WalletView, WalletListView, TransferCoinView, TransferHistoryView, GetWalletName, \
    CourseView, CourseHistoryView

urlpatterns = [
    path("data/list/", DataListView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('wallet/list/', WalletListView.as_view()),
    path('wallet/', WalletView.as_view()),
    path('transfer/', TransferCoinView.as_view()),
    path('transfer/history/', TransferHistoryView.as_view()),
    path('course/', CourseView.as_view()),
]
