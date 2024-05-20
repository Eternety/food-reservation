from rest_framework import serializers

from .models import Food, FoodType, Order

class FoodTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = FoodType
    fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
  type = FoodTypeSerializer()

  class Meta:
    model = Food
    fields = ['id', 'name', 'description', 'price', 'type']

class OrderSerializer(serializers.ModelSerializer):
  
  class Meta: 
    model =  Order 
    fields = ['id', 'name', 'created_at', 'address', 'total_price' , 'discount_applied']


