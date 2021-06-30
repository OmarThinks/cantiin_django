from accounts.models import (User)
from cantiin.models import (Product, Order, Comment)

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ["url", "id", "username", "products","orders"]

class ProductSerializer(serializers.HyperlinkedModelSerializer):
	author = UserSerializer
	class Meta:
		model = Product
		fields = ["url","id","name","price","in_stock","author",
		"comments","created_at","updated_at"]

class OrderSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Order
		fields = ["url","id","product","amount","in_stock",
		"author","created_at","updated_at"]

class CommentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Comment
		fields = ["url","id","product","content","author",
		"created_at","updated_at"]



"""
python manage.py shell
from cantiin.serializers import (UserSerializer, ProductSerializer, OrderSerializer, CommentSerializer)
serializers= [UserSerializer(), ProductSerializer(), OrderSerializer(), CommentSerializer()]
print(repr(serializers[1]))
exit()

from cantiin.serializers import UserSerializerss

"""

