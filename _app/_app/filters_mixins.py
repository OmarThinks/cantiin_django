from django_filters import rest_framework as filters
from accounts.models import (User)
from cantiin.models import (Product, Order, Comment)




class DateTimeFilter(filters.FilterSet):
	min_created_at = filters.DateTimeFilter(field_name="created_at", 
		lookup_expr='gte')
	max_created_at = filters.DateTimeFilter(field_name="created_at", 
		lookup_expr='lte')
	min_updated_at = filters.DateTimeFilter(field_name="updated_at", 
		lookup_expr='gte')
	max_updated_at = filters.DateTimeFilter(field_name="updated_at", 
		lookup_expr='lte')


