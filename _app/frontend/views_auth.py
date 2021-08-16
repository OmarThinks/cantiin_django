from djoser.views import UserViewSet as DjoserViewSet
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from django.http import (HttpResponse, HttpResponseRedirect)
from django.shortcuts import render
from rest_framework import serializers

from django.contrib.auth import views
from django.shortcuts import redirect





class LoginView(views.LoginView):
	extra_context = {"title":"Login"}
	next_page = "/products"
	redirect_authenticated_user = True
	redirect_field_name = "product-list"
	template_name ='pages/login.html'	
	def get_context_data(self, **kwargs):
		context = views.LoginView.get_context_data(self, **kwargs)
		print(context, flush=True)
		print(self.request.__dict__, flush=True)
		return context
	def get_success_url(self):
		return "/products"




def logout(request):
	return redirect("/api-auth/logout/?next=/products/")



















