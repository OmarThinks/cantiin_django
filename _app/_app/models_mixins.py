#Django abstract models TimeStampedModel
from django.db import models
from django.conf import settings



def getTimeStampMixin(nullable):
	class TimeStampMixin(models.Model):
		created_at = models.DateTimeField(auto_now_add=True, null=nullable)
		updated_at = models.DateTimeField(auto_now=True, null=nullable)
		class Meta:
			abstract = True
	return TimeStampMixin
	




def getHasUserForeignKeyMixin(related_name,nullable):
	class HasUserForeignKeyMixin(models.Model):
		author = models.ForeignKey(settings.AUTH_USER_MODEL,
			on_delete=models.CASCADE, related_name=related_name, null=nullable)
		class Meta:
			abstract = True
	return HasUserForeignKeyMixin
