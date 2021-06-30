from accounts.models import (User)
from cantiin.models import (Product, Order, Comment)

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		exclude = ['password',"last_login","is_superuser",
			"first_name","last_name","email","is_staff",
			"is_active","date_joined"]
		depth = 1

class ProductSerializer(serializers.HyperlinkedModelSerializer):
	author = UserSerializer
	class Meta:
		model = Product
		fields = "__all__"
		depth = 1

class OrderSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Order
		fields = "__all__"
		depth = 1

class CommentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Comment
		fields = "__all__"
		depth = 1



"""
python manage.py shell
from cantiin.serializers import (UserSerializer, ProductSerializer, OrderSerializer, CommentSerializer)
serializers= [UserSerializer(), ProductSerializer(), OrderSerializer(), CommentSerializer()]
print(repr(serializers[1]))
exit()

from cantiin.serializers import UserSerializerss

"""

