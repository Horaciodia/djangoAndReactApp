from .views import UserModelListView, GetUser
from django.urls import path

urlpatterns = [
    path('users/', UserModelListView.as_view(), name='users-list'),
    path('getUser/', GetUser.as_view(), name='get-user')
]