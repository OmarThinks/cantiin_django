#Django abstract models TimeStampedModel
from django.db import models
from django.conf import settings


from cantiin.models import Product


class TimeStampMixin():
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class HasUserForeignKeyMixin():
	author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)


class HasProductForeignKeyMixin():
	product = models.ForeignKey(Product, related_name="orders")


