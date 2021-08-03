from accounts.models import (User)
from cantiin.models import (Product, Order, Comment)

from rest_framework import serializers
from my_functions.urls import reverse


class UserSerializer(serializers.HyperlinkedModelSerializer):
	products = serializers.SerializerMethodField(read_only=True)
	def get_products(self,obj):
		return str(reverse(self, 'api:product-list', query_params = {"author":obj.id}))

	products_count = serializers.SerializerMethodField(read_only=True)
	def get_products_count(self,obj):
		return Product.objects.filter(author_id=obj.id).count()


	orders = serializers.SerializerMethodField(read_only=True)
	def get_orders(self,obj):
		return str(reverse(self, 'api:order-list', query_params = {"author":obj.id}))

	orders_count = serializers.SerializerMethodField(read_only=True)
	def get_orders_count(self,obj):
		return Order.objects.filter(author_id=obj.id).count()


	comments = serializers.SerializerMethodField(read_only=True)
	def get_comments(self,obj):
		return str(reverse(self, 'api:comment-list', query_params = {"author":obj.id}))

	comments_count = serializers.SerializerMethodField(read_only=True)
	def get_comments_count(self,obj):
		return Comment.objects.filter(author_id=obj.id).count()


	class Meta:
		model = User
		fields = ["url", "id", "username", "products", "products_count",
			"orders","orders_count","comments","comments_count"]
		extra_kwargs = {'url': {'view_name': 'api:user-detail'}}


class ProductSerializer(serializers.HyperlinkedModelSerializer):
	comments = serializers.SerializerMethodField(read_only=True)
	def get_comments(self,obj):
		return str(reverse(self, 'api:comment-list', 
			query_params = {"product":obj.id}))

	comments_count = serializers.SerializerMethodField(read_only=True)
	def get_comments_count(self,obj):
		return Comment.objects.filter(product_id=obj.id).count()

	orders = serializers.SerializerMethodField(read_only=True)
	def get_orders(self,obj):
		return str(reverse(self, 'api:order-list', 
			query_params = {"product":obj.id}))

	orders_count = serializers.SerializerMethodField(read_only=True)
	def get_orders_count(self,obj):
		return Order.objects.filter(product_id=obj.id).count()

	class Meta:
		model = Product
		fields = ["id","url","name","price","in_stock","author_id","author", 
		"created_at","updated_at","comments","comments_count", 
		"orders","orders_count"]
		extra_kwargs = {
			'author': {'read_only': True, "view_name":"api:user-detail"},
			"url": {"view_name":"api:product-detail"}
			}

class OrderSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Order
		fields = ["url","id","product_id", "product", "unit_price", 
		"amount", "cost", "author_id", "author","created_at","updated_at"]
		extra_kwargs = {'author': {'read_only': True, "view_name":"api:user-detail"},
					"url": {"view_name":"api:order-detail"},
					"product": {"view_name":"api:product-detail"}
			}

class CommentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Comment
		fields = ["url","id","product_id","product","author_id","author",
		"content","created_at","updated_at"]
		extra_kwargs = {'author': {'read_only': True, "view_name":"api:user-detail"},
			"url": {"view_name":"api:comment-detail"},
					"product": {"view_name":"api:product-detail"}

		}

