# This script generates some sample customers, products, and orders
from decimal import Decimal
from datetime import datetime

from django.core.management.base import BaseCommand
from django.db import transaction

from customers.models import Customer
from orders.models import Order, OrderLine
from products.models import Product
from budget.models import SalesTarget

class Command(BaseCommand):
    help = 'Create sample customers, products, and orders'

    def handle(self, *args, **options):

        with transaction.atomic():

            Customer.objects.bulk_create([
                Customer(name='Jane Doe'),
                Customer(name='John Doe'),
            ])
            jane, john = Customer.objects.order_by('name')

            Product.objects.bulk_create([
                Product(name='Apple', price=Decimal('2.50'), inventory=4),
                Product(name='Kiwi', price=Decimal('5.00'), inventory=3),
                Product(name='Orange', price=Decimal('3.00'), inventory=5),
            ])
            apple, kiwi, orange = Product.objects.order_by('name')

            # Jane has placed two orders
            order = Order.objects.create_order(
                customer=jane,
                is_shipped=True,
                created_at=datetime.fromisoformat('2019-04-06T16:00:00+02:00'),
                products=[apple, kiwi],
            )
            Order.objects.create_order(
                customer=jane,
                is_shipped=False,
                created_at=datetime.fromisoformat('2019-04-10T09:00:00+02:00'),
                products=[apple, kiwi],
            )

            # John has placed three orders
            order = Order.objects.create_order(
                customer=john,
                is_shipped=True,
                created_at=datetime.fromisoformat('2019-03-31T15:00:00+01:00'),
                products=[apple, orange],
            )
            order = Order.objects.create_order(
                customer=john,
                is_shipped=True,
                created_at=datetime.fromisoformat('2019-04-01T13:00:00+02:00'),
                products=[orange, kiwi],
            )
            Order.objects.create_order(
                customer=john,
                is_shipped=False,
                created_at=datetime.fromisoformat('2019-04-07T12:00:00+02:00'),
                products=[apple],
            )

            SalesTarget.objects.bulk_create([
                SalesTarget(year=2019, month=3, target=Decimal('10.00')),
                SalesTarget(year=2019, month=4, target=Decimal('12.00')),
            ])
