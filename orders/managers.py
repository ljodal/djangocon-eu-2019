from django.db import models, transaction
from django.db.models.functions import Lag


class OrderQuerySet(models.QuerySet):

    def unshipped(self):
        return self.filter(is_shipped=False)

    def diff_vs_previous_order(self):
        return self.annotate(
            prev_order_id=models.Window(
                expression=Lag('id'),
                partition_by=[models.F('customer_id')],
                order_by=models.F('created_at').asc(),
            )
        )


class OrderManager(models.Manager):

    def create_order(self, products, **kwargs):

        with transaction.atomic():

            # Ensure that we have enough products in inventory
            for product in products:
                product.purchase()

            order = self.create(**kwargs)

            order.lines.bulk_create([
                order.lines.model(
                    order=order,
                    product=product,
                    gross_amount=product.price,
                )
                for product in products
            ])

            return order
