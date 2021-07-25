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
	return render(request, "home.html")

def products_list(request):
	products = Product.objects.order_by("id").all()
	return render(request, "products/list.html",{"products":products})





class ProductDetail(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'products/product_detail.html'

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


