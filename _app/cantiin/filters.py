from django_filters import rest_framework as filters
from accounts.models import (User)
from cantiin.models import (Product, Order, Comment)


class ProductFilter(filters.FilterSet):
	min_price = filters.NumberFilter(field_name="price", 
		lookup_expr='gte')
	max_price = filters.NumberFilter(field_name="price", 
		lookup_expr='lte')

	class Meta:
		model = Product
		fields = ['in_stock', 'min_price', 'max_price',"author_id"]




