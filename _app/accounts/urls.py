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

    def validate_username(self, value):
            username = self.initial_data["username"]
            if(type(username)!=str):
                raise serializers.ValidationError("username should be a string")
            return value
    def validate_password(self, value):
            username = self.initial_data["username"]
            password = self.initial_data["password"]
            if(type(password)!=str):
                raise serializers.ValidationError("password should be a string")
            user = User.objects.filter(username=username).first()
            if user is None:
                raise serializers.ValidationError("wrong username or password")
            if not user.check_password(password):
                raise serializers.ValidationError("wrong username or password")
            return user

#from accounts.urls import LoginSerializer
#serializer = LoginSerializer()
#print(repr(serializer))
@api_view(http_method_names=['POST'])
@authentication_classes([])
@permission_classes([])
def LoginView(request):
    serializer = LoginSerializer(data = request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data
    username = data["username"]
    user = data["password"]
    # This is not the password, this is the user instance
    #print("password", user)
    #print(type(user))
    #print(serializer.__dict__)
    """wrong_password_response = Response()
    wrong_password_response.status_code =400
    wrong_password_response.data = {"password":["wrong username or passwordaaaa"]}
    user = User.objects.filter(username=username).first()
    #print(user)
    if user is None:
        return wrong_password_response
    if not user.check_password(password):
        return wrong_password_response"""
    login(request, user)
    
    #print(data, flush=True)
    return Response({"message": "You are logged in"})







@api_view(http_method_names=["GET"])
def TestLoginView(request):
    print(request.user)
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