"""_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url



from rest_framework import routers
from .views import (homepage, UserViewSet, ProductViewSet, 
	OrderViewSet, CommentViewSet,
	DjoserUserViewSet,ProductViewSetMod, create_product)
from .views_auth import (login, LoginView)

# Routers provide an easy way of automatically determining the URL conf.


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('products', ProductViewSet)
router.register('orders', OrderViewSet)
router.register('comments', CommentViewSet)
#router.register('auth', DjoserUserViewSet)
#router.register('products', ProductViewSetMod)





#from django.contrib.auth import views



urlpatterns = [
	path('', homepage),
	path("products/create", create_product),
	path('', include((router.urls,"cantiin_frontend"), namespace="frontend")),
	path('login/', LoginView.as_view(
		template_name='pages/login_new.html'), name='login'),
]

