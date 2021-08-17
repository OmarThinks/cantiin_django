from cantiin.models import (Product)
from .views import ProductViewSet as _ProductViewSet, generate_custom_renderer
from django.shortcuts import redirect
from django.http import (HttpResponse)
#from pprint import pprint as pp
#pp = pprint.PrettyPrinter(indent=4)
import pprint
pp = pprint.PrettyPrinter(indent=4).pprint



class MyProductsViewSet(_ProductViewSet):
	def get_queryset(self):
		#pp(self.request.__dict__)
		#print(type(self.request.__dict__))
		#pp(self.request.__dict__)
		#pp(["1"])
		#print(self.request, flush=True)
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
