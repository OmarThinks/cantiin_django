from django.shortcuts import render

def about(request):
	return render(request, "about.html")

def homepage(request):
	#return HttpResponse("Home Page")
	return render(request, "home.html",
		{
			"active_main_navbar": "home",
			"title": "Home"
		}			
	)





