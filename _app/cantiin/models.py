from django.db import models

# Create your models here.



#id,name,price,in_stock,seller_id
class Product(models.Model):
    name = models.CharField(max_length=100)
	price = models.FloatField()
    in_stock =  models.BooleanField()

"""
id, user_id, product_id, amount
class Order(db.Model):


id, user_id, product_id, content
class Comments(db.Model):
"""


