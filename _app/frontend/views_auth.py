from djoser.views import UserViewSet as DjoserViewSet
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from django.http import (HttpResponse, HttpResponseRedirect)
from django.shortcuts import render
from rest_framework import serializers

from django.contrib.auth import views
from django.shortcuts import redirect


from my_functions.forms import (form_renderer,
	form_fields_names_list, form_errors_ids_list)


class LoginView(views.LoginView):
	extra_context = {"title":"Login"}
	next_page = "/products"
	redirect_authenticated_user = True
	redirect_field_name = "product-list"
	template_name ='pages/login.html'	
	def get_context_data(self, **kwargs):
		context = views.LoginView.get_context_data(self, **kwargs)
		context["user"] = self.request.user
		#print(context, flush=True)
		#print(self.request.user.is_authenticated, flush=True)
		#print(context["view"].__dict__, flush=True)
		#print(context["request"].user.__dict__,flush=True)
		return context
	def get_success_url(self):
		return "/products"




def logout(request):
	return redirect("/api-auth/logout/?next=/products/")




def signup(request):
	#return HttpResponse("Login")
	#pprint(ProductSerializer().__dict__)
	#pprint(ProductSerializer().__dir__())
	#pprint(ProductSerializer().fields)
	#pprint(ProductSerializer.Meta.__dict__)
	#uctSerializer.__dir__())
	form_list = [
		{	"name":"username",
			"name_capitalized":"Username or Email *",
			"type":"text"
		},
		{	"name":"password",
			"name_capitalized":"Password *",
			"type":"password"
		},
	]
	rendered_form = form_renderer(form_list)
	
	fields_names = form_fields_names_list(form_list)
	errors_ids=form_errors_ids_list(form_list)
	
	#pp(rendered_form)
	#pp(fields_names)
	#pp(errors_ids)

	return render(request, "masters/forms/_general.html",
		{
			"title": "Sign Up",
			"serializer":"",
			"request_destination":"/api/auth/users/",
			"request_method":"POST", 
			"rendered_form":rendered_form,
			"after_scuess_url":"/my_products/",
			"fields_names":fields_names,
			"errors_ids":errors_ids,
			"button_text":"Sign Up",
			"resource_url":"/api/auth/users/"
		})	














