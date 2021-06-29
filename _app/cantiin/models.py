from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


from _app.models_mixins import (TimeStampMixin, 
	HasUserForeignKeyMixin, HasProductForeignKeyMixin)




#id,name,price,in_stock,author
class Product(models.Model, HasUserForeignKeyMixin):
	name = models.CharField(max_length=150)
	price = models.FloatField(
		validators=[MinValueValidator(.1),MaxValueValidator(1000*1000)])
	in_stock =  models.BooleanField()

#id, author, product_id, amount
class Order(models.Model, HasUserForeignKeyMixin, HasProductForeignKeyMixin):
    product = models.ForeignKey(Product, related_name="orders")
	amount = models.IntegerField(
		 validators=[MinValueValidator(1),MaxValueValidator(1000)])

#id, author, product_id, content
class Comment(models.Model, HasUserForeignKeyMixin, HasProductForeignKeyMixin):
    product = models.ForeignKey(Product, related_name="comments")
	name = models.CharField(max_length=1000)




from django.contrib import admin

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Comment)

