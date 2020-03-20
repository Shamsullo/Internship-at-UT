from rest_framework import serializers
from .models import *

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('__all__')
       

class SubCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('__all__')


class CartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cart
        fields = ('__all__')


# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = ('__all__')
            