from django.db import models

from .managers import OrderManager, OrderQuerySet


class Order(models.Model):

    customer = models.ForeignKey('customers.Customer', related_name='orders', on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    is_shipped = models.BooleanField(default=False)

    objects = OrderManager.from_queryset(OrderQuerySet)()


class OrderLine(models.Model):

    order = models.ForeignKey('orders.Order', related_name='lines', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', related_name='order_lines', on_delete=models.PROTECT)
    gross_amount = models.DecimalField(max_digits=10, decimal_places=2)
