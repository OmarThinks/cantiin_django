from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


from my_functions.models_mixins import (getTimeStampMixin, getHasUserForeignKeyMixin)
from rest_framework.reverse import reverse



#id,name,price,in_stock,author
class Product(getHasUserForeignKeyMixin("products"),
	getTimeStampMixin()):
	name = models.CharField(max_length=150)
	price = models.FloatField(
		validators=[MinValueValidator(.1),MaxValueValidator(1000*1000)])
	in_stock =  models.BooleanField()

	def __str__(self):
		return (str(self.id) +") "+ self.name + ", "+ str(self.author))




def getHasProductForeignKeyMixin(related_name, default=None):
	if default == None:
		class HasProductForeignKeyMixin(models.Model):
			product = models.ForeignKey(Product, related_name=related_name,
			on_delete=models.CASCADE)
			class Meta:
				abstract = True
		return HasProductForeignKeyMixin
	class HasProductForeignKeyMixin(models.Model):
		product = models.ForeignKey(Product, related_name=related_name,
		on_delete=models.CASCADE, default =Product.objects.order_by('id').first())
		class Meta:
			abstract = True
	return HasProductForeignKeyMixin


#id, author, product_id, amount
class Order(getHasUserForeignKeyMixin("orders"), 
	getHasProductForeignKeyMixin("orders"), getTimeStampMixin()):
	amount = models.IntegerField(
		 validators=[MinValueValidator(1),MaxValueValidator(1000)])
	@property
	def unit_price(self):
		return self.product.price
	@property
	def cost(self):
		return self.amount*self.product.price
	
	
	def __str__(self):
		return (str(self.product.name) + ", " + str(self.amount) + 
			", " + str(self.author.username))

#id, author, product_id, content
class Comment(getHasUserForeignKeyMixin("comments"), 
	getHasProductForeignKeyMixin("comments"), getTimeStampMixin()):
	content = models.CharField(max_length=1000)

	def __str__(self):
		return (str(self.product.name) + ", " + 
			str(self.author.username) + 
			", " + str(self.content) )



from django.contrib import admin

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Comment)

