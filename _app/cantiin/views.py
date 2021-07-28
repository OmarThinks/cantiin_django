from django.http import HttpResponse
from django.shortcuts import render

from cantiin.models import (Product, Order, Comment)
from rest_framework.renderers import TemplateHTMLRenderer
from .serializers import ProductSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response




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




def abstract_list_renderer(request, items, items_plural, 
	additional_css_files, active_main_navbar, title, item_url_name):
	return render(request, "resources/products/list.html",
		{
			items_plural:items,
			"additional_css_files":additional_css_files,
			"active_main_navbar": active_main_navbar,
			"title": title,
			"item_url_name" : item_url_name
		})





def products_list(request):
	items = Product.objects.order_by("id").all()
	items_plural = "products" 
	additional_css_files = ["/static/css/cards/product.css"]
	active_main_navbar = "products"
	title = "Products List"
	item_url_name = "product-detail"
	return abstract_list_renderer(request, items, items_plural, 
	additional_css_files, active_main_navbar, title, item_url_name)
	"""return render(request, "products/list.html",
		{
			"products":items,
			"additional_css_files":["/static/css/cards/product.css"],
			"active_main_navbar": "products",
			"title": "Products List"
		})"""





class ProductDetail(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'resources/products/product_detail.html'

	def get(self, request, id):
		product = get_object_or_404(Product, pk=id)
		serializer = ProductSerializer(product,context={'request': request})
		return Response({'serializer': serializer, 'product': product})

	def post(self, request, id):
		product = get_object_or_404(Product, pk=id)
		serializer = ProductSerializer(product, data=request.data)
		if not serializer.is_valid():
			return Response({'serializer': serializer, 'product': product})
		serializer.save()
		return redirect('product-list')	



class ProductDetailTest(APIView):
	def get(self, request,id=None):
		return HttpResponse(id)


