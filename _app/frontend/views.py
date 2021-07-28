from django.shortcuts import render


def homepage(request):
	#return HttpResponse("Home Page")
	return render(request, "pages/home.html",
		{
			"active_main_navbar": "home",
			"title": "Home"
		}			
	)





