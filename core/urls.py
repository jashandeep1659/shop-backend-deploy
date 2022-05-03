from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

# creating router object
router = DefaultRouter()
# register viewset with routers
router.register("product", ProductList, basename="productapi")
router.register("brand", BrandWiseList, basename="brandlist")
# router.register('product/<int:id>',ProductList, basename='productapi')
urlpatterns = [
    # path('products', ProductList.as_view()),
    path("", include(router.urls)),
    path("banner/", BannerDetail.as_view()),
    path("user/create/", UserCreater.as_view()),
    # path("brand/<str:slug>/", BrandWiseList.as_view()),
]
