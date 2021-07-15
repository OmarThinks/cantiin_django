from rest_framework import serializers
from django_restql.mixins import DynamicFieldsMixin

from cantiin.models import (Product, Order, Comment)
from accounts.models import User

from cantiin.serializers import (UserSerializer,
	ProductSerializer, OrderSerializer, CommentSerializer)

class graphqlUserSerializer(DynamicFieldsMixin, UserSerializer):
	pass





class graphqlProductSerializer(DynamicFieldsMixin, 
	ProductSerializer):
	pass




class graphqlOrderSerializer(DynamicFieldsMixin, 
	OrderSerializer):
	pass

class graphqlCommentSerializer(DynamicFieldsMixin, 
	CommentSerializer):
	pass









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
    products = SerializerMethodField(read_only=True)
    products_count = SerializerMethodField(read_only=True)
    orders = SerializerMethodField(read_only=True)
    orders_count = SerializerMethodField(read_only=True)
    comments = SerializerMethodField(read_only=True)
    comments_count = SerializerMethodField(read_only=True)

>>> graphqlProductSerializer():
    id = IntegerField(label='ID', read_only=True)
    url = HyperlinkedIdentityField(view_name='product-detail')
    name = CharField(max_length=150)
    price = FloatField(max_value=1000000, min_value=0.1)
    in_stock = BooleanField()
    author_id = ReadOnlyField()
    author = HyperlinkedRelatedField(read_only=True, view_name='user-detail')
    created_at = DateTimeField(read_only=True)
    updated_at = DateTimeField(read_only=True)
    comments = SerializerMethodField(read_only=True)
    comments_count = SerializerMethodField(read_only=True)
    orders = SerializerMethodField(read_only=True)
    orders_count = SerializerMethodField(read_only=True)

>>> graphqlOrderSerializer():
    url = HyperlinkedIdentityField(view_name='order-detail')
    id = IntegerField(label='ID', read_only=True)
    product_id = ReadOnlyField()
    product = HyperlinkedRelatedField(queryset=Product.objects.all(), view_name='product-detail')
    unit_price = ReadOnlyField()
    amount = IntegerField(max_value=1000, min_value=1)
    cost = ReadOnlyField()
    author_id = ReadOnlyField()
    author = HyperlinkedRelatedField(read_only=True, view_name='user-detail')
    created_at = DateTimeField(read_only=True)
    updated_at = DateTimeField(read_only=True)

>>> graphqlCommentSerializer():
    url = HyperlinkedIdentityField(view_name='comment-detail')
    id = IntegerField(label='ID', read_only=True)
    product_id = ReadOnlyField()
    product = HyperlinkedRelatedField(queryset=Product.objects.all(), view_name='product-detail')
    author_id = ReadOnlyField()
    author = HyperlinkedRelatedField(read_only=True, view_name='user-detail')
    content = CharField(max_length=1000)
    created_at = DateTimeField(read_only=True)
    updated_at = DateTimeField(read_only=True)




"""





