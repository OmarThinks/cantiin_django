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



from .views import (homepage)

from .views_products import (products_list, ProductDetail, ProductDetailTest)
from .views_users import (users_list)



urlpatterns = [
	path('', homepage),
	path('products/', products_list),
	path('users/', users_list),
	path('productss/<int:id>/', ProductDetail.as_view(), 
		name="product-detail-test"),
	path('productsss/<int:id>/', ProductDetailTest.as_view()),
	]

#    path('productss/<int:pk>', ProductDetail),
#    url(r'^productss/(?P<pk>[0-9]+)/$', ProductDetail),