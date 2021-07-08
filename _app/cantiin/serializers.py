from accounts.models import (User)
from cantiin.models import (Product, Order, Comment)

from rest_framework import serializers
from my_functions.urls import reverse


class UserSerializer(serializers.HyperlinkedModelSerializer):
	products = serializers.SerializerMethodField(read_only=True)
	def get_products(self,obj):
		return str(reverse(self, 'product-list', query_params = {"author":obj.id}))
	orders = serializers.SerializerMethodField(read_only=True)
	def get_orders(self,obj):
		return str(reverse(self, 'order-list', query_params = {"author":obj.id}))
	comments = serializers.SerializerMethodField(read_only=True)
	def get_comments(self,obj):
		return str(reverse(self, 'comment-list', query_params = {"author":obj.id}))
	class Meta:
		model = User
		fields = ["url", "id", "username", "products","orders","comments"]

class ProductSerializer(serializers.HyperlinkedModelSerializer):
	comments = serializers.SerializerMethodField(read_only=True)
	def get_comments(self,obj):
		return str(reverse(self, 'comment-list', 
			query_params = {"product":obj.id}))
	orders = serializers.SerializerMethodField(read_only=True)
	def get_orders(self,obj):
		return str(reverse(self, 'order-list', 
			query_params = {"product":obj.id}))
	class Meta:
		model = Product
		fields = ["id","url","name","price","in_stock","author_id","author", 
		"created_at","updated_at","comments", "orders"]

class OrderSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Order
		fields = ["url","id","product_id", "product", "amount",
		"author_id", "author","created_at","updated_at"]

class CommentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Comment
		fields = ["url","id","product_id","product","author_id","author",
		"content","created_at","updated_at"]



"""
python manage.py shell
from cantiin.serializers import (UserSerializer, ProductSerializer, OrderSerializer, CommentSerializer)
serializers= [UserSerializer(), ProductSerializer(), OrderSerializer(), CommentSerializer()]
print(repr(serializers[0]),"\n")
print(repr(serializers[1]),"\n")
print(repr(serializers[2]),"\n")
print(repr(serializers[3]),"\n")
exit()








>>> >>> >>> UserSerializer():
	url = HyperlinkedIdentityField(view_name='user-detail')
	id = IntegerField(label='ID', read_only=True)
	username = CharField(help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, validators=[<django.contrib.auth.validators.UnicodeUsernameValidator object>, <UniqueValidator(queryset=User.objects.all())>])
	products = HyperlinkedRelatedField(many=True, queryset=Product.objects.all(), view_name='product-detail')
	orders = HyperlinkedRelatedField(many=True, queryset=Order.objects.all(), view_name='order-detail')

>>> ProductSerializer():
	url = HyperlinkedIdentityField(view_name='product-detail')
	id = IntegerField(label='ID', read_only=True)
	name = CharField(max_length=150)
	price = FloatField(max_value=1000000, min_value=0.1)
	in_stock = BooleanField()
	author = HyperlinkedRelatedField(queryset=User.objects.all(), view_name='user-detail')
	comments = HyperlinkedRelatedField(many=True, queryset=Comment.objects.all(), view_name='comment-detail')
	created_at = DateTimeField(read_only=True)
	updated_at = DateTimeField(read_only=True)

>>> OrderSerializer():
	url = HyperlinkedIdentityField(view_name='order-detail')
	id = IntegerField(label='ID', read_only=True)
	product = HyperlinkedRelatedField(queryset=Product.objects.all(), view_name='product-detail')
	amount = IntegerField(max_value=1000, min_value=1)
	author = HyperlinkedRelatedField(queryset=User.objects.all(), view_name='user-detail')
	created_at = DateTimeField(read_only=True)
	updated_at = DateTimeField(read_only=True)

>>> CommentSerializer():
	url = HyperlinkedIdentityField(view_name='comment-detail')
	id = IntegerField(label='ID', read_only=True)
	product = HyperlinkedRelatedField(queryset=Product.objects.all(), view_name='product-detail')
	content = CharField(max_length=1000)
	author = HyperlinkedRelatedField(queryset=User.objects.all(), view_name='user-detail')
	created_at = DateTimeField(read_only=True)
	updated_at = DateTimeField(read_only=True)
















"""

