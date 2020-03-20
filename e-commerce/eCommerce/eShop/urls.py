
from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('items', views.ItemView, basename='items')
router.register('categories', views.CategoryView, basename='cats')
router.register('subcats', views.SubCatView, basename='subcats')
router.register('cart', views.CartView, basename='cart')
# router.register('orders', views.OrderView, basename='orders')


urlpatterns = [
    path(r'', include(router.urls)),

]   