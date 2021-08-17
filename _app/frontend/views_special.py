from cantiin.models import (Product)
from .views import ProductViewSet as _ProductViewSet
from django.shortcuts import redirect
from django.http import (HttpResponse)


class MyProductsViewSet(_ProductViewSet):
	def get_queryset(self):
		print(self.request.user.__dir__(),flush=True)
		return _ProductViewSet.get_queryset(self)



def my_products(request):
	if not request.user.is_authenticated:
		return redirect("/products/")
	user_id = request.user.id
	products = Product.objects.filter(author_id=user_id).all()
	print(products, flush=True)
	return HttpResponse("My Products")
