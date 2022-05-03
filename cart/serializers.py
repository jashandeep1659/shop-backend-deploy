from rest_framework import serializers
from .models import *
from user.models import User


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart_item
        fields = "__all__"
        depth = 1
