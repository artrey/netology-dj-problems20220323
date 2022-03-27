from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    # id
    name = models.CharField(max_length=60)
    price = models.IntegerField(validators=[MinValueValidator(1)])
    # orders
    # positions


class Order(models.Model):
    products = models.ManyToManyField(Product, related_name='orders',
                                      through='OrderPosition')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='orders',
                             null=True, blank=True)


class OrderPosition(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              related_name='positions')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='positions')
    qty = models.IntegerField(validators=[MinValueValidator(1)],
                              default=1)
