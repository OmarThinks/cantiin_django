from .models import (User)
from rest_framework import serializers
from django.urls import path

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
            """
            """
            username = self.initial_data["username"]
            password = self.initial_data["password"]
            if(type(password)!=str):
                raise serializers.ValidationError("password should be a string")
            print(self.initial_data["password"], flush=True)
            
            # Is this the correct password?
            user = User.objects.filter(username==username).first()

            if user is None:
                raise serializers.ValidationError('wrong username or password')

            if not user.check_password(password):
                raise serializers.ValidationError('wrong username or password')
            return value

#from accounts.urls import LoginSerializer
#serializer = LoginSerializer()
#print(repr(serializer))
@api_view(http_method_names=["GET",'POST'])
@authentication_classes([])
@permission_classes([])
def login(request):
    serializer = LoginSerializer(data = request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data
    print(data, flush=True)
    return Response({"message": "Hello, world!"})















urlpatterns = [
	path('api/auth/custom/login/', login),
]