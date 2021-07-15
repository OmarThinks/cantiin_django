from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	def __str__(self):
		return self.username
	

from django.contrib import admin

admin.site.register(User)
