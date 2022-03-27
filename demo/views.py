from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet

from demo.models import Order, Product
from demo.serializers import ProductSerializer


def orders_view(request):
    context = {
        'orders': Order.objects.all(),
    }
    return render(request, 'index.html', context)


def add_products_view(request):
    Product.objects.update_or_create(
        id=10,
        defaults={'name': 'Продукт 1', 'price': 2000}
    )
    return redirect(orders_view)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer