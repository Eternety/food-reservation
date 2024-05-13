from django.contrib import admin

from .models import Food, FoodType, Discount, Reservation

@admin.register(FoodType)
class FoodTypeAdmin(admin.ModelAdmin):
	list_display = ('id', 'name',)
	search_fields = ('name',)


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'price' ,'type',)
	search_fields = ('name',)
	list_filter = ('type',)
	date_hierarchy = 'created_at'

@admin.register(Discount)
class Discount(admin.ModelAdmin):
	list_display = ('min_total_price', 'discount_percentage',)
	date_hierarchy = 'created_at'
	
@admin.register(Reservation)
class Reservation(admin.ModelAdmin):
	list_display = ('id', 'customer', 'reservation_at', 'number_of_guests','foods','description','created_at','updated_at',)
	search_fields = ('id',)
	list_filter = ('created_at',)
	date_hierarchy = 'created_at'
	
