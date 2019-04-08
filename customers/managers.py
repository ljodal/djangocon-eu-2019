from django.db import models, transaction
from django.db.models.functions import Lag

from orders.models import Order


class CustomerQuerySet(models.QuerySet):

    def with_latest_order_time(self):
        return self.annotate(
            latest_order_time=models.Subquery(
                Order.objects.filter(
                    customer=models.OuterRef('pk'),
                ).order_by(
                    '-created_at'
                ).values(
                    'created_at'
                )[:1]
            )
        )
