from rest_framework import serializers
from django_restql.mixins import DynamicFieldsMixin

from cantiin.models import (Product, Order, Comment)
from accounts.models import User


class graphUserSerializer(DynamicFieldsMixin, 
	serializer.ModelSerializer):

	products_count = serializers.SerializerMethodField(read_only=True)
	def get_products_count(self,obj):
		return Product.objects.filter(author_id=obj.id).count()

	orders_count = serializers.SerializerMethodField(read_only=True)
	def get_orders_count(self,obj):
		return Order.objects.filter(author_id=obj.id).count()

	comments_count = serializers.SerializerMethodField(read_only=True)
	def get_comments_count(self,obj):
		return Comment.objects.filter(author_id=obj.id).count()

	class Meta:
		model = User
		fields = ["url", "id", "username", "products", "products_count",
			"orders","orders_count","comments","comments_count"]
	class Meta:
		model = Location
		fields = ['id', 'country',  'city', 'street']






class ProductSerializer(DynamicFieldsMixin, 
	serializer.ModelSerializer):
	comments_count = serializers.SerializerMethodField(read_only=True)
	def get_comments_count(self,obj):
		return Comment.objects.filter(product_id=obj.id).count()

	orders_count = serializers.SerializerMethodField(read_only=True)
	def get_orders_count(self,obj):
		return Order.objects.filter(product_id=obj.id).count()

	class Meta:
		model = Product
		fields = ["id","url","name","price","in_stock","author_id","author", 
		"created_at","updated_at","comments","comments_count", 
		"orders","orders_count"]
		extra_kwargs = {'author': {'read_only': True}}




class OrderSerializer(DynamicFieldsMixin, 
	serializer.ModelSerializer):
	class Meta:
		model = Order
		fields = ["url","id","product_id", "product", "unit_price", 
		"amount", "cost", "author_id", "author","created_at","updated_at"]
		extra_kwargs = {'author': {'read_only': True}}

class CommentSerializer(DynamicFieldsMixin, 
	serializer.ModelSerializer):
	class Meta:
		model = Comment
		fields = ["url","id","product_id","product","author_id","author",
		"content","created_at","updated_at"]
		extra_kwargs = {'author': {'read_only': True}}











