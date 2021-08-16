from djoser.views import UserViewSet as DjoserViewSet
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import serializers


class AuthViewSet(DjoserViewSet):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'base_layout.html'	
		



class LoginSerializer(serializers.Serializer):
    Username_or_Email = serializers.CharField(
        max_length=100,
        style={'placeholder': 'Username or Email', 'autofocus': True}
    )
    password = serializers.CharField(
        max_length=100,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    remember_me = serializers.BooleanField()


def login(request):
	#return HttpResponse("Login")
	return render(request, "pages/login.html",
		{
			"active_main_navbar": "login",
			"title": "Login",
			"serializer":LoginSerializer
		}			
	)

def login_old(request):
	#return HttpResponse("Login")
	return render(request, "pages/login.html",
		{
			"active_main_navbar": "login",
			"title": "Login"
		}			
	)





