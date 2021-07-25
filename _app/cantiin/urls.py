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

from .rest_views import (
    UserViewSet, ProductViewSet, OrderViewSet, CommentViewSet)

from .views import (about, homepage, products_list, ProductDetail, ProductDetailTest)


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('products', ProductViewSet)
router.register('orders', OrderViewSet)
router.register('comments', CommentViewSet)




urlpatterns = [
    path('api/', include(router.urls)),
    path('', homepage),
    path('about/', about),
    path('products/', products_list),
    path('productss/<int:id>/', ProductDetail.as_view(), 
        name="product-detail-test"),
    path('productsss/<int:id>/', ProductDetailTest.as_view()),

]

#    path('productss/<int:pk>', ProductDetail),
#    url(r'^productss/(?P<pk>[0-9]+)/$', ProductDetail),
