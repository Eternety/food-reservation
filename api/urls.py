from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'food-types', views.FoodTypeListViewSet)
router.register(r'foods', views.FoodListViewSet)
router.register(r'user-types', views.UserTypeTypeListViewSet)
router.register(r'customers', views.CustomUserListViewSet)
router.register(r'orders', views.OrderListViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
