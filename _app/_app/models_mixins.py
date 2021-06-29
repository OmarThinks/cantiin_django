#Django abstract models TimeStampedModel
from django.db import models
from django.conf import settings




class TimeStampMixin(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	class Meta:
		abstract = True




def getHasUserForeignKeyMixin(related_name):
	class HasUserForeignKeyMixin(models.Model):
		author = models.ForeignKey(settings.AUTH_USER_MODEL,
			on_delete=models.CASCADE, related_name=related_name)
		class Meta:
			abstract = True

	return HasUserForeignKeyMixin
