from django.contrib import admin

from .models import Food, FoodType

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
