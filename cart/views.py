from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from user.models import User
from .serializers import *
from rest_framework import generics
from .models import *
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class CartList(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        user = request.user
        cart = Cart.objects.filter(user=user)
        if len(cart) == 0:
            Cart.objects.create(user=request.user)
        cart = cart.reverse()[0]
        queryset = Cart_item.objects.filter(cart=cart.id)
        serializer = CartSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def update(self, request, pk=None):
        user = request.user
        action = request.data["action"]
        item = get_object_or_404(Cart_item, id=pk)
        cart = Cart.objects.filter(user=user)
        if len(cart) == 0:
            Cart.objects.create(user=request.user)
        cart = cart.reverse()[0]
        if item.cart == cart:
            if action == "add":
                item.quantity = item.quantity + 1
                item.save()

            if action == "minus" and item.quantity > 1:
                item.quantity = item.quantity - 1
                item.save()
        queryset = Cart_item.objects.filter(cart=cart.id)
        serializer = CartSerializer(queryset)
        return Response(serializer.data)

    def create(self, request):
        queryset = Cart_item.objects.all()
        data = request.data
        user = request.user
        cart = Cart.objects.filter(user=user)
        if len(cart) == 0:
            Cart.objects.create(user=request.user)
        cart = cart.reverse()[0]
        try:
            cart_item = Cart_item.objects.get(cart_id=cart.id, product=data["id"])
            serializer = CartSerializer(cart_item)
            return Response(serializer.data)
        except:
            cart_item = Cart_item.objects.create(
                product_id=data["id"], quantity=data["quantity"], cart=cart
            )
            serializer = CartSerializer(cart_item)
            return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = get_object_or_404(Cart_item, id=pk)
        serializer = CartSerializer(queryset)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        user = request.user
        item = get_object_or_404(Cart_item, id=pk)
        cart = Cart.objects.filter(user=user)
        if len(cart) == 0:
            Cart.objects.create(user=request.user)
        cart = cart.reverse()[0]
        if item.cart == cart:
            item.delete()
        queryset = Cart_item.objects.filter(cart=cart.id)
        serializer = CartSerializer(queryset)
        return Response(serializer.data)


# from django.shortcuts import render, get_object_or_404
# from rest_framework import viewsets
# from rest_framework.response import Response
# from user.models import User
# from rest_framework import mixins
# from .serializers import *
# from rest_framework import generics
# from .models import *


# class CartList(
#     mixins.ListModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView,
# ):
#     queryset = Cart_item.objects.all()
#     serializer_class = CartSerializer

#     def get(self, request):
#         # queryset = self.get_queryset
#         # queryset = Cart.objects.filter(user=1)
#         # queryset = queryset.reverse()[0]
#         queryset = Cart_item.objects.all()
#         serializer = CartSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         queryset = Cart_item.objects.all()
#         serializer = CartSerializer(queryset)
#         return Response(serializer.data)

#     def put(self, request):
#         queryset = Cart_item.objects.all()
#         serializer = CartSerializer(queryset)
#         return Response(serializer.data)
