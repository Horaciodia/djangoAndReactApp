from rest_framework import generics
from .models import Post, Comment
from .serializers import UserSerializer, PostSerializer
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse
import json, uuid

class UserModelListView(generics.ListCreateAPIView):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))            
            username = data.get('username')

            if User.objects.filter(username=username).exists():
                return JsonResponse({'message': 'User already exists'})

            user = User.objects.create(
                username=username,
                password=make_password(data.get('password')),
                first_name=data.get('firstName'),
                last_name=data.get('lastName')
            )

            return JsonResponse({'message': 'User created successfully'})
        except Exception as e:
            print("Error processing POST request:", str(e))
            return JsonResponse({'error': 'Internal server error'}, status=500)

    def get(self, request, *args, **kwargs):
        username = request.GET.get('username')
        password = request.GET.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)   

            if user is not None:
                return JsonResponse({'message': 'Success'})   
            else:
                return JsonResponse({
                    'Invalid credentials': [password, username]
                })

class GetUser(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        username = request.GET.get('username')
        try:
            user = User.objects.get(username=username)
            serializer = UserSerializer(user)
            return JsonResponse(serializer.data)
        except:
            return JsonResponse({'error': 'No user with that username'})

class CreatePost(generics.ListCreateAPIView):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode('utf-8'))            
        title = data.get('title')
        content = data.get('content')

        Post.objects.create(
            title=title,
            content=content,
            postId=uuid.uuid4()
        )

        getPost = Post.objects.get(title=title)
        getPostSerializer = PostSerializer(getPost)

        return JsonResponse(getPostSerializer.data)

class GetPost(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        postId = request.GET.get('postId')

        post = Post.objects.get(postId=postId)
        postSerialized = PostSerializer(post)

        return JsonResponse(postSerialized.data)

class CreateComment(generics.ListCreateAPIView):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode('utf-8'))
        content = data.get('comment')
        postId = data.get('post')

        post = Post.objects.get(postId=postId)
        #comment = Comment.objects.new(
        #    post=post,
        #    user=
        #)


