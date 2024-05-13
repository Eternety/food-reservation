from django.db import models

from django.contrib.auth.models import AbstractUser

class UserType(models.Model):
  """Model for storing different user types (customer, admin, etc.)"""
  name = models.CharField(max_length=50)
  
  def __str__(self):
    return self.name

class CustomUser(AbstractUser):
  user_type = models.ForeignKey(UserType, on_delete=models.CASCADE, null=True, blank=True)


class UserProfile(models.Model):
  """Model for storing additional customer profile information"""
  user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  address = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.user.username} Profile"

class FoodType(models.Model):
  """Model for storing different food types (appetizer, main course, etc.)"""
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Food(models.Model):
  """Model for storing individual food items"""
  name = models.CharField(max_length=100)
  description = models.TextField(blank=True)
  price = models.PositiveIntegerField()
  type = models.ForeignKey(FoodType, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class Reservation(models.Model):
  """Model for storing food reservation details"""
  customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  reservation_at = models.DateTimeField()
  number_of_guests = models.PositiveIntegerField()
  foods = models.ManyToManyField(Food)
  description = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.customer.username} - {self.reservation_at}"

class Discount(models.Model):
  """Model for storing discount tiers"""
  min_total_price = models.PositiveIntegerField()
  discount_percentage = models.PositiveIntegerField()

  def __str__(self):
    return f"Discount: ${self.min_total_price} and above - {self.discount_percentage}%"

class Order(models.Model):
  """Model for storing food order details"""
  reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  address = models.CharField(max_length=255)
  total_price = models.PositiveIntegerField()
  discount_applied = models.PositiveIntegerField()

  def __str__(self):
    return f"Order for reservation {self.reservation.id}"