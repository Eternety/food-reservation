from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'food-types', views.FoodTypeListViewSet)
router.register(r'foods', views.FoodListViewSet)
router.register(r'user-type', views.UserTypeTypeListViewSet)
router.register(r'customer-user', views.CustomUserListViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
