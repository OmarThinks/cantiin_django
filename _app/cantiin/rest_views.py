from rest_framework import viewsets
from rest_framework.mixins import (ListModelMixin, RetrieveModelMixin)
from rest_framework.renderers import TemplateHTMLRenderer
from django_filters.rest_framework import DjangoFilterBackend

from accounts.models import (User)
from cantiin.models import (Product, Order, Comment)
from cantiin.serializers import (
	UserSerializer, ProductSerializer, OrderSerializer, CommentSerializer)
from .filters import (UserFilter,ProductFilter,
	OrderFilter,CommentFilter)
from rest_framework import filters

from my_functions.viewset_mixins import HasAuthorViewsetMixin


# ViewSets define the view behavior.
class UserViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	filterset_class = UserFilter	
	filter_backends = [DjangoFilterBackend, filters.SearchFilter]
	search_fields = ["username"]

class ProductViewSet(HasAuthorViewsetMixin):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	filterset_class = ProductFilter	
	filter_backends = [DjangoFilterBackend, filters.SearchFilter]
	search_fields = ["name"]

	"""def post(self, request, format=None):
		serializer = ProductSerializer(data=request.data, 
			context={'author': request.user})
		if serializer.is_valid():
			serializer.save(author = request.user)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""

class OrderViewSet(HasAuthorViewsetMixin):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
	filterset_class = OrderFilter

class CommentViewSet(HasAuthorViewsetMixin):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	filterset_class = CommentFilter	
	filter_backends = [DjangoFilterBackend, filters.SearchFilter]
	search_fields = ["content"]
