from .models import (User)
from rest_framework import serializers
from django.urls import path
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from django.contrib.auth.validators import UnicodeUsernameValidator

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, validators=[UnicodeUsernameValidator])
    password = serializers.CharField(max_length=128)


@api_view(http_method_names=['POST'])
@authentication_classes([])
@permission_classes([])
def LoginView(request):
    serializer = LoginSerializer(data = request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data
    username, password = data["username"], data['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({"message": "You are logged in"})
    wrong_password_response = Response(status=400,  data={"password":["wrong username or password"]})
    return wrong_password_response







@api_view(http_method_names=["GET"])
def TestLoginView(request):
    #print(request.user)
    if(request.user.is_authenticated):
        return Response({"message": "You are logged in"})
    return Response({"message": "You are logged out"})




def emptyview(request):
    return "Hey"







from rest_framework.authtoken import views

urlpatterns = [
	path('api/auth/custom/login/', LoginView),
	path('api/auth/custom/login/test/', TestLoginView),
    path('api-token-auth/', views.obtain_auth_token),
    path('emptyview/', emptyview),
 
]