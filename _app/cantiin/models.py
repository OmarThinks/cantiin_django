from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


from _app.models_mixins import (TimeStampMixin, getHasUserForeignKeyMixin)




#id,name,price,in_stock,author
class Product(models.Model,getHasUserForeignKeyMixin("products"),
	TimeStampMixin):
	name = models.CharField(max_length=150)
	price = models.FloatField(
		validators=[MinValueValidator(.1),MaxValueValidator(1000*1000)])
	in_stock =  models.BooleanField()


def getHasProductForeignKeyMixin(related_name):
	class HasProductForeignKeyMixin():
		product = models.ForeignKey(Product, related_name=related_name,
		on_delete=models.CASCADE)

	return HasProductForeignKeyMixin


#id, author, product_id, amount
class Order(models.Model,getHasUserForeignKeyMixin("orders"), 
	getHasProductForeignKeyMixin("orders"), TimeStampMixin):
	amount = models.IntegerField(
		 validators=[MinValueValidator(1),MaxValueValidator(1000)])

#id, author, product_id, content
class Comment(models.Model,getHasUserForeignKeyMixin("comments"), 
	getHasProductForeignKeyMixin("comments"), TimeStampMixin):
	name = models.CharField(max_length=1000)




from django.contrib import admin

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Comment)

