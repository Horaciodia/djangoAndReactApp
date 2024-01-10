from rest_framework import generics
from .models import UserModel
from .serializers import UserModelSerializer
from django.contrib.auth.hashers import check_password, make_password
import json
from django.http import JsonResponse

class UserModelListView(generics.ListCreateAPIView):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))            
            username = data.get('username')

            if UserModel.objects.filter(username=username).exists():
                return JsonResponse({'message': 'User already exists'})

            user = UserModel.objects.create(
                username=username,
                password=make_password(data.get('password')),
                firstName=data.get('firstName'),
                lastName=data.get('lastName')
            )

            return JsonResponse({'message': 'User created successfully'})
        except Exception as e:
            print("Error processing POST request:", str(e))
            return JsonResponse({'error': 'Internal server error'}, status=500)

    def get(self, request, *args, **kwargs):
        username = request.GET.get('username')
        password = request.GET.get('password')

        if username and password:
            try:
                user = UserModel.objects.get(username=username)
            except UserModel.DoesNotExist:
                return JsonResponse({'message': 'Invalid username'})

            if check_password(password, user.password):
                serializer = UserModelSerializer(user)
                return JsonResponse(serializer.data)
            else:
                return JsonResponse({'message': 'Invalid password'})            

    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer