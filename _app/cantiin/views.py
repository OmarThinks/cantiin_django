from django.shortcuts import render

from rest_framework import viewsets
# Serializers define the API representation.


from accounts.models import (User)
from cantiin.models import (Product, Order, Comment)

from cantiin.serializers import (
	UserSerializer, ProductSerializer, OrderSerializer, CommentSerializer)

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



# Routers provide an easy way of automatically determining the URL conf.





