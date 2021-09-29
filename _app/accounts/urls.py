from .models import (User)
from rest_framework import serializers
from django.urls import path

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

class LoginSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ["username", "password"]




@api_view(http_method_names=["GET",'POST'])
@authentication_classes([])
@permission_classes([])
def login(request):
    return Response({"message": "Hello, world!"})



urlpatterns = [
	path('api/auth/custom/login/', login),
]