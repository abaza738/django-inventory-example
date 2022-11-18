from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .models import Ingredient, Order, Product
from .serializers import (IngredientSerializer, OrderSerializer,
                          ProductSerializer)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def ingredients(request):
    ingredients = Ingredient.objects.all()
    serializer = IngredientSerializer(ingredients, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def get_ingredient(request, id):
    ingredient = get_object_or_404(Ingredient.objects, pk=id)
    serializer = IngredientSerializer(ingredient)
    return Response(serializer.data)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def get_product(request, id):
    product = get_object_or_404(Product.objects, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def orders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def get_order(request, id):
    order = get_object_or_404(Order.objects, pk=id)
    serializer = OrderSerializer(order)
    return Response(serializer.data)
