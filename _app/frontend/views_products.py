from django.http import HttpResponse
from django.shortcuts import render

from cantiin.models import (Product, Order, Comment)
from rest_framework.renderers import TemplateHTMLRenderer
from cantiin.serializers import ProductSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
# Create your views here.

from .abstract_renderers import abstract_list_renderer


def products_list(request):
	items = Product.objects.order_by("id").all()
	list_template_link = "resources/products/list.html"
	items_plural = "products" 
	additional_css_files = []
	active_main_navbar = "products"
	title = "Products List"
	item_url_name = "product-detail"
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














# /productss/2
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





