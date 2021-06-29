#Django abstract models TimeStampedModel
from django.db import models
from django.conf import settings

import datetime

from accounts.models import User



def getTimeStampMixin():
	class TimeStampMixin(models.Model):
		created_at = models.DateTimeField(auto_now_add=True)
		updated_at = models.DateTimeField(auto_now=True)
		class Meta:
			abstract = True
	return TimeStampMixin







def getHasUserForeignKeyMixin(related_name,default = None):
	if default == None:
		class HasUserForeignKeyMixin(models.Model):
			author = models.ForeignKey(settings.AUTH_USER_MODEL,
				on_delete=models.CASCADE, related_name=related_name)
			class Meta:
				abstract = True
		return HasUserForeignKeyMixin
	class HasUserForeignKeyMixin(models.Model):
		author = models.ForeignKey(settings.AUTH_USER_MODEL,
			on_delete=models.CASCADE, related_name=related_name, 
			default=User.objects.order_by('id').first())
		class Meta:
			abstract = True
	return HasUserForeignKeyMixin
