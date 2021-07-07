from django_filters import rest_framework as filters
from accounts.models import (User)
from cantiin.models import (Product, Order, Comment)




class DateTimeFilter(filters.FilterSet):
	min_created_at = filters.DateFilter(field_name="created_at", 
		lookup_expr='gte')
	max_created_at = filters.DateFilter(field_name="created_at", 
		lookup_expr='lte')
	min_updated_at = filters.DateFilter(field_name="updated_at", 
		lookup_expr='gte')
	max_updated_at = filters.DateFilter(field_name="updated_at", 
		lookup_expr='lte')




class IdFilter(filters.FilterSet):
	min_id = filters.DateFilter(field_name="id", 
		lookup_expr='gte')
	max_id = filters.DateFilter(field_name="id", 
		lookup_expr='lte')

