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
	search = filters.CharFilter(method='my_custom_filter',label="Search")	
	min_price = filters.NumberFilter(field_name="price", 
		lookup_expr='gte')
	max_price = filters.NumberFilter(field_name="price", 
		lookup_expr='lte')
	in_stock = filters.BooleanFilter(field_name="in_stock")
	class Meta:
		model = Product
		fields = "__all__"
	def my_custom_filter(self, queryset, name, value):
		return Product.objects.filter(Q(name__icontains=value))


class OrderFilter(IdFilter, DateTimeFilter):
	min_amount = filters.NumberFilter(field_name="amount", 
		lookup_expr='gte')
	max_amount = filters.NumberFilter(field_name="amount", 
		lookup_expr='lte')
	class Meta:
		model = Order
		fields = "__all__"


class CommentFilter(IdFilter, DateTimeFilter):
	search = filters.CharFilter(method='my_custom_filter',label="Search")	
	class Meta:
		model = Comment
		fields = "__all__"
	def my_custom_filter(self, queryset, name, value):
		return Comment.objects.filter(Q(content__icontains=value))



