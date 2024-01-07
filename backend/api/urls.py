from .views import UserModelListView
from django.urls import path

urlpatterns = [
    path('users/', UserModelListView.as_view(), name='users-list')
]