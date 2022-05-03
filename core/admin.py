from django.contrib import admin

from .models import *
class ProductImage(admin.TabularInline):
    	model = Product_Image
    	raw_id_fields = ['product']

class ProductPoint(admin.TabularInline):
    model = Product_Point
    raw_id_fields = ['product']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','brand','price']
    prepopulated_fields= {'slug':('name',),}
    inlines = [ProductPoint,ProductImage ]

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',),}

@admin.register(Category)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',),}
admin.site.register(Product_Image)
admin.site.register(Product_Point) 

admin.site.register(Banner)