from django.contrib import admin

from .models import Food, FoodType, UserType, CustomUser

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
	

@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
	list_display = ('id', 'name',)
	search_fields = ('name',)

@admin.register(CustomUser)
class CustomerUserAdmin(admin.ModelAdmin):
	list_display = ('id', 'user_type',)
	search_fields = ('user_type',)
