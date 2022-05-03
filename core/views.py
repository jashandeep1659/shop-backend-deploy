from django.shortcuts import render, get_object_or_404
from .serializers import *
from user.models import User
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from datetime import datetime
import math
import random
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.permissions import IsAdminUser


class ProductList(viewsets.ViewSet):
    lookup_field = "slug"
    # permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = Product.objects.all()
        serializer = Product_serializer(
            queryset, many=True, context={"request": request}
        )
        return Response(serializer.data)

    def retrieve(self, request, slug=None):
        print(request.user)
        queryset = Product.objects.all()
        product = get_object_or_404(Product, slug=slug)
        serializer = ProdcutDetial_serializer(product, context={"request": request})
        return Response(serializer.data)


class BannerDetail(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerDetail_serialzers

    def list(self, request):
        queryset = Banner.objects.all()
        banner = get_object_or_404(Banner, id=1)
        serializer = BannerDetail_serialzers(banner, context={"request": request})
        return Response(serializer.data)


class UserCreater(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetail_serializers

    def post(self, request):
        data = request.data
        email = data["email"]
        full_name = data["full_name"]
        password = data["password"]
        user = User.objects.create(email=email, full_name=full_name)
        user.set_password(password)
        user.is_active = False

        def genrate_otp():
            digits = "0123456789"
            OTP = ""
            for i in range(4):
                OTP += digits[math.floor(random.random() * 10)]
            return OTP

        genrate_otp()
        user.otp = genrate_otp()
        user.otp_bring_time = datetime.now()
        user.otp_expired = False
        user.is_active = False
        subject_message = "Login your acco  unt"
        main_message = f"Here's the otp to login in your account {user.otp}. if this is not done by you then just ignore this message and please don't share this otp with anyone"
        send_mail(
            f"{subject_message}",
            f"{main_message}",
            settings.EMAIL_HOST_USER,
            ["jjashan505@gmail.com"],
            fail_silently=False,
        )
        user.save()
        user.delete()
        return Response({"data": "this"})


class UserVerifier(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetail_serializers

    def post(self, request):
        pass


class BrandWiseList(viewsets.ViewSet):
    lookup_field = "slug"

    def list(self, request):
        # brand = get_object_or_404(Brand, slug=slug)
        # products = Product.objects.filter(brand=brand)
        brands = Brand.objects.all()
        serializer = BrandWiseList_serializers(
            brands, many=True, context={"request": request}
        )
        return Response(serializer.data)

    def retrieve(self, request, slug=None):
        brand = get_object_or_404(Brand, slug=slug)
        products = Product.objects.filter(brand=brand)
        serializer = Product_serializer(
            products, many=True, context={"request": request}
        )
        return Response(serializer.data)

    # serializers


"""

{
    "full_name": "jashan",
    "email": "jashan@jj.com",
    "password": "45"
}
"""
