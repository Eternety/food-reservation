from django.shortcuts import render

from rest_framework import viewsets

from .models import Food, FoodType, Order
from .serializers import FoodSerializer, FoodTypeSerializer ,OrderSerializer

class FoodTypeListViewSet(viewsets.ReadOnlyModelViewSet):
	"""API endpoint to list all food types"""
	queryset = FoodType.objects.all()
	serializer_class = FoodTypeSerializer

class FoodListViewSet(viewsets.ReadOnlyModelViewSet):
	"""API endpoint to list all food items"""
	queryset = Food.objects.all()
	serializer_class = FoodSerializer

class OrderListViewSet(viewsets.ReadOnlyModelViewSet):
	"""API endpoint to list all order items"""
	queryset = Order.objects.all()
	serializer_class = OrderSerializer