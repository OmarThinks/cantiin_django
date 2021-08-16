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
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		current_site = get_current_site(self.request)
		context.update({
			self.redirect_field_name: self.get_redirect_url(),
			'site': current_site,
			'site_name': current_site.name,
			**(self.extra_context or {})
		})
		return context



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





