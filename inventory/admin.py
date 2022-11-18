from django.contrib import admin

from .models import (Ingredient, Order, OrderProducts, Product,
                     ProductIngredients)


class ProductIngredientsInline(admin.TabularInline):
    model = ProductIngredients


class OrderProductsInline(admin.TabularInline):
    model = OrderProducts


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductIngredientsInline]


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderProductsInline]


admin.site.register(Ingredient)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
