from django.http import HttpResponse
from django.shortcuts import render

def about(request):
	return render(request, "about.html")

def homepage(request):
	#return HttpResponse("Home Page")
	return render(request, "home.html")

