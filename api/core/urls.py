from django.urls import path, include
from .views import DataDetailView, DataListView

urlpatterns = [path("data/", DataDetailView.as_view()),
               path("data/list/", DataListView.as_view()),
               ]
