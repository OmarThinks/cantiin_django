from django.http import HttpResponse

def about(request):
	return HttpResponse("About")

def homepage(request):
	return HttpResponse("Home Page")
