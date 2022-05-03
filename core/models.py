from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    special_line = models.CharField(max_length=150)
    older_price = models.IntegerField()
    price = models.IntegerField()
    detail = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    card_banner = models.ImageField(upload_to="images/product")
    large_baner = models.ImageField(upload_to="images/product")
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Product_Image(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_images"
    )
    image = models.ImageField(upload_to="images/product")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Product_Point(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=10)
    detial = models.CharField(max_length=10)
    updated = models.DateTimeField(auto_now=True)


class Banner(models.Model):
    name = models.CharField(max_length=50)
    special_line = models.CharField(max_length=150)
    product_image = models.ImageField(upload_to="images/banner")
    link = models.CharField(max_length=150)
