from rest_framework import serializers
from django_restql.mixins import DynamicFieldsMixin

from cantiin.models import (Product, Order, Comment)
from accounts.models import User


class graphqlUserSerializer(DynamicFieldsMixin, 
	serializers.ModelSerializer):

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
		extra_kwargs = {
			'products': {'read_only': True},
			"comments": {'read_only': True},
			"orders": {'read_only': True},
		}





class graphqlProductSerializer(DynamicFieldsMixin, 
	serializers.ModelSerializer):
	comments_count = serializers.SerializerMethodField(read_only=True)
	def get_comments_count(self,obj):
		return Comment.objects.filter(product_id=obj.id).count()

	orders_count = serializers.SerializerMethodField(read_only=True)
	def get_orders_count(self,obj):
		return Order.objects.filter(product_id=obj.id).count()

	class Meta:
		model = Product
		fields = ["id","url","name","price","in_stock","author", 
		"created_at","updated_at","comments","comments_count", 
		"orders","orders_count"]
		extra_kwargs = {
			'author': {'read_only': True},
			"comments": {'read_only': True},
			"orders": {'read_only': True},
		}




class graphqlOrderSerializer(DynamicFieldsMixin, 
	serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = ["url","id", "product", "unit_price", 
		"amount", "cost", "author","created_at","updated_at"]
		extra_kwargs = {'author': {'read_only': True}}

class graphqlCommentSerializer(DynamicFieldsMixin, 
	serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ["url","id","product","author",
		"content","created_at","updated_at"]
		extra_kwargs = {'author': {'read_only': True}}









"""
python manage.py shell
from cantiin.graphql_serializers import (graphqlUserSerializer, graphqlProductSerializer, graphqlOrderSerializer, graphqlCommentSerializer)
serializers= [graphqlUserSerializer(), graphqlProductSerializer(), graphqlOrderSerializer(), graphqlCommentSerializer()]
print(repr(serializers[0]),"\n")
print(repr(serializers[1]),"\n")
print(repr(serializers[2]),"\n")
print(repr(serializers[3]),"\n")
exit()






>>> >>> >>> 

graphqlUserSerializer():
    url = HyperlinkedIdentityField(view_name='user-detail')
    id = IntegerField(label='ID', read_only=True)
    username = CharField(help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, validators=[<django.contrib.auth.validators.UnicodeUsernameValidator object>, <UniqueValidator(queryset=User.objects.all())>])
    products = PrimaryKeyRelatedField(many=True, read_only=True)
    products_count = SerializerMethodField(read_only=True)
    orders = PrimaryKeyRelatedField(many=True, read_only=True)
    orders_count = SerializerMethodField(read_only=True)
    comments = PrimaryKeyRelatedField(many=True, read_only=True)
    comments_count = SerializerMethodField(read_only=True)

>>> graphqlProductSerializer():
    id = IntegerField(label='ID', read_only=True)
    url = HyperlinkedIdentityField(view_name='product-detail')
    name = CharField(max_length=150)
    price = FloatField(max_value=1000000, min_value=0.1)
    in_stock = BooleanField()
    author = PrimaryKeyRelatedField(read_only=True)
    created_at = DateTimeField(read_only=True)
    updated_at = DateTimeField(read_only=True)
    comments = PrimaryKeyRelatedField(many=True, read_only=True)
    comments_count = SerializerMethodField(read_only=True)
    orders = PrimaryKeyRelatedField(many=True, read_only=True)
    orders_count = SerializerMethodField(read_only=True)

>>> graphqlOrderSerializer():
    url = HyperlinkedIdentityField(view_name='order-detail')
    id = IntegerField(label='ID', read_only=True)
    product = PrimaryKeyRelatedField(queryset=Product.objects.all())
    unit_price = ReadOnlyField()
    amount = IntegerField(max_value=1000, min_value=1)
    cost = ReadOnlyField()
    author = PrimaryKeyRelatedField(read_only=True)
    created_at = DateTimeField(read_only=True)
    updated_at = DateTimeField(read_only=True)

>>> graphqlCommentSerializer():
    url = HyperlinkedIdentityField(view_name='comment-detail')
    id = IntegerField(label='ID', read_only=True)
    product = PrimaryKeyRelatedField(queryset=Product.objects.all())
    author = PrimaryKeyRelatedField(read_only=True)
    content = CharField(max_length=1000)
    created_at = DateTimeField(read_only=True)
    updated_at = DateTimeField(read_only=True)

>>>



"""





