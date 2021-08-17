from cantiin.models import (Product)
from .views import ProductViewSet as _ProductViewSet
from django.shortcuts import redirect
from django.http import (HttpResponse)


class MyProductsViewSet(_ProductViewSet):
	def get_queryset(self):
		user_id = self.request.user.id
		return Product.objects.filter(author_id=user_id).all()

my_products = MyProductsViewSet.as_view({"get":"list"})
