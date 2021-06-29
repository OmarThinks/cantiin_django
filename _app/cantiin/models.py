from django.db import models

# Create your models here.




"""
class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3)
    birth_date = models.DateField(blank=True, null=True)
"""




"""

class User(db.Model):
    # Autoincrementing, unique primary key
    id = Column(Integer(), primary_key=True)
    # String username
    username = Column(String(), unique=True, nullable=False)
    # username could be like "fish"
    # username has to be unique
    # not allowing several users to have the same username
    password =  Column(String(), unique=False, nullable=False)
    # Password is a string
    # Example: "12345", "abc"
    # it doesn't have to be unique

    products = db.relationship("Product",backref="seller")
    orders = db.relationship("Order",backref="buyer")
    images = db.relationship("Image",backref="seller")




'''
Product
a persistent product entity, extends the base SQLAlchemy Model
id,name,price,in_stock,seller_id
'''
class Product(db.Model):
    # Autoincrementing, unique primary key
    id = Column(Integer(), primary_key=True)
    # String name
    name = Column(String(), unique=False, nullable=False)
    # name could be like "Labtop"
    # name dowsn't have to be unique
    # allowing several users to sell the same product
    price =  Column(Float(), unique=False, nullable=False)
    # Price is a float
    # Example: 5.0, 6.0 , 50.0, 0.5
    # It should be float, allowing things with low
    # price to be sold
    in_stock =  Column(Boolean(), unique=False, 
        nullable=False, default=True)
    # in_stock is a boolean
    # Example: True, False
    # it represents whether this product is for sale or not
    # True = For sale, can be displayed to customers
    # False = now for sale, can not be displayed to customers
    seller_id = Column(Integer(),db.ForeignKey("user.id"),
     unique=False, nullable=False)
    #seller_id = Column(Integer(), unique=False, nullable=False)
    # seller_id
    # This is the id of the seller user
    # The user who sells this product
    # it is an integer
    # Example: 1, 2 or 3
    
    orders = db.relationship("Order",backref="product")


Order:
id, user_id, product_id, amount
class Order(db.Model):
    # Autoincrementing, unique primary key
    id = Column(Integer(), primary_key=True)
    # String name
    user_id =Column(Integer(),db.ForeignKey("user.id"),
     unique=False, nullable=False)
    # user_id
    # This is the id of the user who ordered the products
    # it is an integer
    # Example: 1, 2 or 3
    product_id  = Column(Integer,db.ForeignKey("product.id"))
    # product_id is an integer 
    # it refers to the product.id in the products table
    # Example: 1, 2 , 3
    amount =  Column(Integer(), unique=False, nullable=False)
    # amount is an integer
    # Example: 5, 6, 50
    total_cost = 0.0
'''
Image
a persistent product entity, extends the base SQLAlchemy Model
id,seller_id,name,formatting
The image will be stroed with it's id
'''
class Image(db.Model):
    # Autoincrementing, unique primary key
    id = Column(Integer(), primary_key=True)
    seller_id = Column(Integer(),db.ForeignKey("user.id"),
     unique=False, nullable=False)
    # This is the id of the seller user
    # The user who sells this product
    # it is an integer
    # Example: 1, 2 or 3
    name = Column(String(), unique=False, nullable=False)
    # image name could be like "fish"
    # image name can not to be unique
    # not allowing several users to have the same username
    formatting =  Column(String(), unique=False, nullable=False)
    # formattng is a string that represents the type of image
    # There can be only 2 types: "png" , "jpg"
    # it can not be unique

"""



