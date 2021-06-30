from django.http import HttpResponse
from django.shortcuts import render

from cantiin.models import (Product, Order, Comment)



def about(request):
	return render(request, "about.html")

def homepage(request):
	#return HttpResponse("Home Page")
	return render(request, "home.html")

def products_list(request):
	products = Product.objects.order_by("id").all()
	return render(request, "products/list.html",{"products":products})

