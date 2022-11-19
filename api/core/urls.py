from django.urls import path, include
from .views import DataListView
from .views import ProfileView, WalletView, WalletListView, TransferCoinView, TransferHistoryView, GetWalletName, \
    CourseView, CourseHistoryView

urlpatterns = [
    path("data/list/", DataListView.as_view()),
    path('profile/', ProfileView.as_view()),
    # path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]
