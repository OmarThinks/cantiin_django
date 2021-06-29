from accounts.models import (User)
from cantiin.models import (Product, Order, Comment)

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ["id",'url', 'username']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = "__all__"
		depth = 1

class OrderSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = "__all__"
		depth = 1

class CommentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = "__all__"
		depth = 1
