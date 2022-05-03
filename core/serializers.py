from rest_framework import serializers
from .models import *
from user.models import User


class ProductImages_serializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Image
        fields = "__all__"


class ProductPoints_serializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Point
        files = "__all__"


class Product_serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        depth = 1


class ProdcutDetial_serializer(serializers.ModelSerializer):
    product_images = ProductImages_serializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"
        depth = 1
        extra_kwargs = {"url": {"lookup_field": "slug"}}


class BannerDetail_serialzers(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


class UserDetail_serializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["full_name", "email", "password"]


class BrandWiseList_serializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"
        depth = 1
