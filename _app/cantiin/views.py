from django.http import HttpResponse
from django.shortcuts import render

def about(request):
	return HttpResponse("About")

def homepage(request):
	#return HttpResponse("Home Page")
	return render(request, "home.html")

