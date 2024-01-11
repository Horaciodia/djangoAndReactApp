from .views import UserModelListView, GetUser, CreatePost, GetPost
from django.urls import path

urlpatterns = [
    path('users/', UserModelListView.as_view(), name='users-list'),
    path('getUser/', GetUser.as_view(), name='get-user'),
    path('createPost/', CreatePost.as_view(), name='new-post'),
    path('getPost/', GetPost.as_view(), name='get-post')
]