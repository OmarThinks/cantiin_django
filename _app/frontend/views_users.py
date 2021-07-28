from django.http import HttpResponse
from django.shortcuts import render

from accounts.models import (User)
from rest_framework.renderers import TemplateHTMLRenderer
from cantiin.serializers import UserSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
# Create your views here.

from .abstract_renderers import abstract_list_renderer


def users_list(request):
	items = User.objects.order_by("id").all()
	list_template_link = "resources/users/list.html"
	items_plural = "users" 
	additional_css_files = []
	active_main_navbar = "users"
	title = "Users List"
	item_url_name = "user-detail"
	return abstract_list_renderer(request, list_template_link, 
		items, items_plural, additional_css_files, 
		active_main_navbar, title, item_url_name)
	"""return render(request, "products/list.html",
		{
			"products":items,
			"additional_css_files":["/static/css/cards/product.css"],
			"active_main_navbar": "products",
			"title": "Products List"
		})"""




