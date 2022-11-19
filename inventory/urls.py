from django.urls import path
from .views import ingredients, get_ingredient, products, get_product, orders, get_order, exportExcelIngredients

urlpatterns = [
    path('ingredients/', ingredients),
    path('excel/ingredients/', exportExcelIngredients),
    path('ingredients/<str:id>', get_ingredient),
    path('products', products),
    path('products/<str:id>', get_product),
    path('orders', orders),
    path('orders/<str:id>', get_order),
]