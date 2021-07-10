from accounts.models import (User)
from cantiin.models import (Product, Order, Comment)

from rest_framework import serializers
from my_functions.urls import reverse


class UserSerializer(serializers.HyperlinkedModelSerializer):
	products = serializers.SerializerMethodField(read_only=True)
	def get_products(self,obj):
		return str(reverse(self, 'product-list', query_params = {"author":obj.id}))

	products_count = serializers.SerializerMethodField(read_only=True)
	def get_products_count(self,obj):
		return Product.objects.filter(author_id=obj.id).count()


	orders = serializers.SerializerMethodField(read_only=True)
	def get_orders(self,obj):
		return str(reverse(self, 'order-list', query_params = {"author":obj.id}))

	orders_count = serializers.SerializerMethodField(read_only=True)
	def get_orders_count(self,obj):
		return Order.objects.filter(author_id=obj.id).count()


	comments = serializers.SerializerMethodField(read_only=True)
	def get_comments(self,obj):
		return str(reverse(self, 'comment-list', query_params = {"author":obj.id}))

	comments_count = serializers.SerializerMethodField(read_only=True)
	def get_comments_count(self,obj):
		return Comment.objects.filter(author_id=obj.id).count()


	class Meta:
		model = User
		fields = ["url", "id", "username", "products", "products_count",
			"orders","orders_count","comments","comments_count"]

class ProductSerializer(serializers.HyperlinkedModelSerializer):
	comments = serializers.SerializerMethodField(read_only=True)
	def get_comments(self,obj):
		return str(reverse(self, 'comment-list', 
			query_params = {"product":obj.id}))

	comments_count = serializers.SerializerMethodField(read_only=True)
	def get_comments_count(self,obj):
		return Comment.objects.filter(product_id=obj.id).count()

	orders = serializers.SerializerMethodField(read_only=True)
	def get_orders(self,obj):
		return str(reverse(self, 'order-list', 
			query_params = {"product":obj.id}))

	orders_count = serializers.SerializerMethodField(read_only=True)
	def get_orders_count(self,obj):
		return Order.objects.filter(product_id=obj.id).count()

	"""def create(self, validated_data):
		#validated_data["author"] = author
		return Product(**validated_data#, author = self.context.author
			)"""
	class Meta:
		model = Product
		fields = ["id","url","name","price","in_stock","author_id","author", 
		"created_at","updated_at","comments","comments_count", 
		"orders","orders_count"]
		extra_kwargs = {'author': {'read_only': True}}

class OrderSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Order
		fields = ["url","id","product_id", "product", "unit_price", 
		"amount", "cost", "author_id", "author","created_at","updated_at"]
		extra_kwargs = {'author': {'read_only': True}}

class CommentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Comment
		fields = ["url","id","product_id","product","author_id","author",
		"content","created_at","updated_at"]
		extra_kwargs = {'author': {'read_only': True}}



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
	products = SerializerMethodField(read_only=True)
	products_count = SerializerMethodField(read_only=True)
	orders = SerializerMethodField(read_only=True)
	orders_count = SerializerMethodField(read_only=True)
	comments = SerializerMethodField(read_only=True)
	comments_count = SerializerMethodField(read_only=True)

>>> ProductSerializer():
	id = IntegerField(label='ID', read_only=True)
	url = HyperlinkedIdentityField(view_name='product-detail')
	name = CharField(max_length=150)
	price = FloatField(max_value=1000000, min_value=0.1)
	in_stock = BooleanField()
	author_id = ReadOnlyField()
	author = HyperlinkedRelatedField(queryset=User.objects.all(), view_name='user-detail')
	created_at = DateTimeField(read_only=True)
	updated_at = DateTimeField(read_only=True)
	comments = SerializerMethodField(read_only=True)
	comments_count = SerializerMethodField(read_only=True)
	orders = SerializerMethodField(read_only=True)
	orders_count = SerializerMethodField(read_only=True)

>>> OrderSerializer():
	url = HyperlinkedIdentityField(view_name='order-detail')
	id = IntegerField(label='ID', read_only=True)
	product_id = ReadOnlyField()
	product = HyperlinkedRelatedField(queryset=Product.objects.all(), view_name='product-detail')
	amount = IntegerField(max_value=1000, min_value=1)
	author_id = ReadOnlyField()
	author = HyperlinkedRelatedField(queryset=User.objects.all(), view_name='user-detail')
	created_at = DateTimeField(read_only=True)
	updated_at = DateTimeField(read_only=True)

>>> CommentSerializer():
	url = HyperlinkedIdentityField(view_name='comment-detail')
	id = IntegerField(label='ID', read_only=True)
	product_id = ReadOnlyField()
	product = HyperlinkedRelatedField(queryset=Product.objects.all(), view_name='product-detail')
	author_id = ReadOnlyField()
	author = HyperlinkedRelatedField(queryset=User.objects.all(), view_name='user-detail')
	content = CharField(max_length=1000)
	created_at = DateTimeField(read_only=True)
	updated_at = DateTimeField(read_only=True)


"""

