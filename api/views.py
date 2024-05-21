from django.shortcuts import render

from rest_framework import viewsets


from .models import Food, FoodType, UserType, CustomUser, Order
from .serializers import FoodSerializer, FoodTypeSerializer, UserTypeSerializer, CustomUserSerializer, OrderSerializer

class FoodTypeListViewSet(viewsets.ReadOnlyModelViewSet):
	"""API endpoint to list all food types"""
	queryset = FoodType.objects.all()
	serializer_class = FoodTypeSerializer

class FoodListViewSet(viewsets.ReadOnlyModelViewSet):
	"""API endpoint to list all food items"""
	queryset = Food.objects.all()
	serializer_class = FoodSerializer

	
class UserTypeTypeListViewSet(viewsets.ReadOnlyModelViewSet):
	"""API endpoint to list all User types"""
	queryset = UserType.objects.all()
	serializer_class = UserTypeSerializer

class CustomUserListViewSet(viewsets.ReadOnlyModelViewSet):
	"""API endpoint to list all CustomUser items"""
	queryset = CustomUser.objects.all()
	serializer_class = CustomUserSerializer


class OrderListViewSet(viewsets.ReadOnlyModelViewSet):
	"""API endpoint to list all order items"""
	queryset = Order.objects.all()
	serializer_class = OrderSerializer