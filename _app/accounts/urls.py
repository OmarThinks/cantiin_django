from .models import (User)
from rest_framework import serializers
from django.urls import path
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from cantiin.serializers import UserSerializer
from django.contrib.auth.validators import UnicodeUsernameValidator

from django.contrib.auth.models import AnonymousUser

from cantiin.serializers import UserSerializer

from rest_framework.exceptions import AuthenticationFailed



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
    return Response(status=400,  data={"password":["wrong username or password"]})




@api_view(http_method_names=['GET',"POST"])
def logout_view(request):
    if type(request.user)==AnonymousUser:
        return Response({"message":"you are alreeady logged out"})
    logout(request)
    return Response({"message":"you logged Out successfully"})




@api_view(http_method_names=['GET'])
def UserWho(request):
    if type(request.user)==AnonymousUser:
        return Response(status = 401, data ={"message":"you are logged out"})
    #user = User.objects.filter(id=payload['id']).first()
    #serializer = 
    return Response(UserSerializer(request.user,context={'request': request}).data)




urlpatterns = [
	path('api/auth/custom/login/', LoginView),
	path('api/auth/custom/logout/', logout_view),
 	path('api/auth/custom/user/', UserWho),

]