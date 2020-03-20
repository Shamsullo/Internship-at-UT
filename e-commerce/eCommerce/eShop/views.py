from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response


from .models import *
from .serializers import *
# Create your views here.


class ItemView(viewsets.ModelViewSet):
    # try:
    queryset = Item.objects.all()
    # except Item.DoesNotExist:
    # return Response(staus=status.HTTP_404_NOT_FOUND)

    serializer_class = ItemSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCatView(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCatSerializer


class CartView(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    # price_to_pay = 0
    # for i in queryset:
    #     price_to_pay += i.price_to_pay
    serializer_class = CartSerializer


# class OrderView(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
