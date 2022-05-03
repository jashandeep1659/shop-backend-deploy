from django.contrib import admin

from .models import *


class CartItems(admin.TabularInline):
    model = Cart_item
    raw_id_fields = ["cart"]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    # list_display = ['name','brand','price']
    inlines = [
        CartItems,
    ]


admin.site.register(Cart_item)
admin.site.register(Order)
admin.site.register(Order_item)
