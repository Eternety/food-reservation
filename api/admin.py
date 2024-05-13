from django.contrib import admin

from .models import Food, FoodType, Order

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


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ('id', 'reservation', 'total_price' ,)
	search_fields = ('reservation',)
	date_hierarchy = 'created_at'


