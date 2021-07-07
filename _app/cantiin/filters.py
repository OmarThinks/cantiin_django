from django_filters import rest_framework as filters
from accounts.models import (User)
from cantiin.models import (Product, Order, Comment)
from _app.filters_mixins import DateTimeFilter



class ProductFilter(DateTimeFilter):
	min_price = filters.NumberFilter(field_name="price", 
		lookup_expr='gte')
	max_price = filters.NumberFilter(field_name="price", 
		lookup_expr='lte')
	in_stock = filters.BooleanFilter(field_name="in_stock")
	class Meta:
		model = Product
		fields = ['in_stock', "author_id"]




