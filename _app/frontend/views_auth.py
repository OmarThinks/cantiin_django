from djoser.views import UserViewSet as DjoserViewSet
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rest_framework import serializers


class AuthViewSet(DjoserViewSet):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'base_layout.html'	
		



class LoginSerializer(serializers.Serializer):
	username = serializers.CharField(
		max_length=100,
		style={'placeholder': 'Username or Email', 'autofocus': True,
		"name":"username", "tag":"username"
		}
	)
	password = serializers.CharField(
		max_length=100,
		style={'input_type': 'password', 'placeholder': 'Password'}
	)
	remember_me = serializers.BooleanField()

#from django.contrib.auth import views
from django.contrib.auth import views
class LoginView(views.LoginView):
	extra_context = {"title":"Login"}
	next_page = "/"
	redirect_authenticated_user = True
	redirect_field_name = "/"
	
	def dispatch(self, request, *args, **kwargs):
		if self.request.user.is_authenticated:
			return HttpResponseRedirect("/")
		return super().dispatch(request, *args, **kwargs)
	
	def get_context_data(self, **kwargs):
		context = views.LoginView.get_context_data(self, **kwargs)
		print(context, flush=True)
		print(context["form"].__dict__)
		return context
	def get_success_url(self):
		return "/"


def login(request):
	#return HttpResponse("Login")
	#print(request.method, flush=True)
	#return views.LoginView(template_name='pages/login.html'), name='login')
	if(request.method=="GET"):
		return render(request, "pages/login.html",
			{
				"active_main_navbar": "login",
				"title": "Login",
				"serializer":LoginSerializer,
				"method":"POST",
				#"request_to":"/login/",
				"request_to":"/api-auth/login?format=json",
				"next":""
			}			
		)
	else:
		return HttpResponse("Hey")




def login_old(request):
	#return HttpResponse("Login")
	#print(request.method, flush=True)
	if(request.method=="GET"):
		return render(request, "pages/login.html",
			{
				"active_main_navbar": "login",
				"title": "Login",
				"serializer":LoginSerializer,
				"method":"POST",
				#"request_to":"/login/",
				"request_to":"/api-auth/login",
				"next":""
			}			
		)
	else:
		return HttpResponse("Hey")

def login_old(request):
	#return HttpResponse("Login")
	return render(request, "pages/login.html",
		{
			"active_main_navbar": "login",
			"title": "Login"
		}			
	)





