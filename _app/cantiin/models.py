from django.db import models

# Create your models here.

#id,name,price,in_stock,author
class Product(models.Model):
	name = models.CharField(max_length=150)
	price = models.FloatField()
	in_stock =  models.BooleanField()

#id, author, product_id, amount
class Order(models.Model):
	amount = models.IntegerField()

#id, author, product_id, content
class Comment(models.Model):
	name = models.CharField(max_length=1000)
