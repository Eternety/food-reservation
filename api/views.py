from django.shortcuts import render

from rest_framework import viewsets

from .models import Food, FoodType, UserType, CustomUser
from .serializers import FoodSerializer, FoodTypeSerializer, UserTypeSerializer, CustomUserSerializer

class FoodTypeListViewSet(viewsets.ReadOnlyModelViewSet):
	"""API endpoint to list all food types"""
	queryset = FoodType.objects.all()
	serializer_class = FoodTypeSerializer

class UserTypeListViewSet(viewsets.ReadOnlyModelViewSet):
	"""API endpoint to list all food items"""
	queryset = UserType.objects.all()
	serializer_class = FoodSerializer
	
class UserTypeTypeListViewSet(viewsets.ReadOnlyModelViewSet):
	"""API endpoint to list all User types"""
	queryset = UserType.objects.all()
	serializer_class = UserTypeSerializer

class CustomUserListViewSet(viewsets.ReadOnlyModelViewSet):
	"""API endpoint to list all CustomUser items"""
	queryset = CustomUser.objects.all()
	serializer_class = CustomUserSerializer