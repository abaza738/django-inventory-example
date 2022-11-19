import mimetypes
import os
import pandas
import time

from django.http.response import HttpResponse
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


@api_view(['GET'])
def exportExcelIngredients(request):
    ingredients = Ingredient.objects.all()
    serializer = IngredientSerializer(ingredients, many=True)

    supposedly_unique_slug_for_the_file_name = int(time.time())
    file_name = f'ingredients_{supposedly_unique_slug_for_the_file_name}.xlsx'
    file_path = f'temp/{file_name}'
    mime_type = mimetypes.guess_type(file_path)

    pandas.DataFrame(serializer.data).to_excel(file_path, index=False)

    binary_content = open(file_path, 'rb').read()
    os.remove(file_path)

    response = HttpResponse(binary_content, content_type=mime_type)
    response['Content-Disposition'] = f'attachment; filename={file_name}'

    return response
