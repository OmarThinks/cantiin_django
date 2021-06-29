from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

from django.contrib import admin

admin.site.register(User)
