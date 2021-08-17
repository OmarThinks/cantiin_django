from cantiin.models import (Product)
from .views import ProductViewSet as _ProductViewSet, generate_custom_renderer
from django.shortcuts import redirect
from django.http import (HttpResponse)


class MyProductsViewSet(_ProductViewSet):
	def get_queryset(self):
		print(self.__dir__(), flush=True)
		user_id = self.request.user.id
		return Product.objects.filter(author_id=user_id).all()
	def get_renderers(self):
		customRenderer = generate_custom_renderer(
			items_plural="products",active_main_navbar= "my_products",
			title="My Products", additional_css_files=[], 
			item_url_name="frontend:product-detail")
		renderers = [customRenderer]
		return [renderer() for renderer in renderers]

my_products = MyProductsViewSet.as_view({"get":"list"})
