from rest_framework import viewsets
from rest_framework.mixins import (ListModelMixin, RetrieveModelMixin)
from rest_framework.renderers import TemplateHTMLRenderer
from django_filters.rest_framework import DjangoFilterBackend

from accounts.models import (User)
from cantiin.models import (Product, Order, Comment)
from cantiin.serializers import (
	UserSerializer, ProductSerializer, OrderSerializer, CommentSerializer)
from .filters import (ProductFilter,OrderFilter,CommentFilter)
from rest_framework import filters


# ViewSets define the view behavior.
class UserViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	filterset_class = ProductFilter	
	filter_backends = [DjangoFilterBackend, filters.SearchFilter]
	search_fields = ["name"]

class OrderViewSet(viewsets.ModelViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
	filterset_class = OrderFilter	

class CommentViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	filterset_class = CommentFilter	
	filter_backends = [DjangoFilterBackend, filters.SearchFilter]
	search_fields = ["content"]
