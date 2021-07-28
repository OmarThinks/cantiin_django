from django.shortcuts import render

# Create your views here.



from cantiin.views import UserViewSet as _UserViewSet
from cantiin.views import ProductViewSet as _ProductViewSet
from cantiin.views import OrderViewSet as _OrderViewSet
from cantiin.views import CommentViewSet as _CommentViewSet
from rest_framework.renderers import TemplateHTMLRenderer



def base_page(request):
	#return HttpResponse("Home Page")
	return render(request, "base.html")




class UserViewSet(_UserViewSet):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'base.html'

class ProductViewSet(_ProductViewSet):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'base.html'

class OrderViewSet(_OrderViewSet):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'base.html'

class CommentViewSet(_CommentViewSet):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'base.html'








