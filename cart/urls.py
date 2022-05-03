from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

# creating router object
router = DefaultRouter()
router.register("cart", CartList, basename="cart")
urlpatterns = [
    # path('products', ProductList.as_view()),
    path("", include(router.urls)),
]
