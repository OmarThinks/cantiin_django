from django_filters import rest_framework as filters
from accounts.models import (User)
from cantiin.models import (Product, Order, Comment)
from _app.filters_mixins import (DateTimeFilter, IdFilter)

from accounts.models import (User)

from django.db.models import Q


class UserFilter(IdFilter):
	search = filters.CharFilter(method='my_custom_filter',label="Search")	
	class Meta:
		model = User
		fields = ["id", "username","search"]

	def my_custom_filter(self, queryset, name, value):
		return User.objects.filter(Q(username__icontains=value))

# https://stackoverflow.com/a/57270647/14819065






class ProductFilter(IdFilter, DateTimeFilter):
	name = filters.CharFilter(lookup_expr='icontains')
	min_price = filters.NumberFilter(field_name="price", 
		lookup_expr='gte')
	max_price = filters.NumberFilter(field_name="price", 
		lookup_expr='lte')
	in_stock = filters.BooleanFilter(field_name="in_stock")
	class Meta:
		model = Product
		fields = "__all__"


class OrderFilter(IdFilter, DateTimeFilter):
	min_amount = filters.NumberFilter(field_name="amount", 
		lookup_expr='gte')
	max_amount = filters.NumberFilter(field_name="amount", 
		lookup_expr='lte')
	class Meta:
		model = Order
		fields = "__all__"


class CommentFilter(IdFilter, DateTimeFilter):
	content = filters.CharFilter(lookup_expr='icontains')
	class Meta:
		model = Comment
		fields = "__all__"



