from django.db import models
from django.db.models.functions import ExtractYear, ExtractMonth
from orders.models import Order


class MonthlyBudgetQuerySet(models.QuerySet):

    def with_gross_total_sales(self):

        subquery = Order.objects.filter(
            created_at__year=models.OuterRef('year'),
            created_at__month=models.OuterRef('month'),
        ).values(
            year=ExtractYear('created_at'),
            month=ExtractMonth('created_at'),
        ).annotate(
            gross_total=models.Sum('lines__gross_amount'),
        ).values(
            'gross_total',
        )

        return self.annotate(
            gross_total_sales=models.Subquery(subquery),
        )

    def with_weekend_sales(self):

        subquery = Order.objects.filter(
            created_at__year=models.OuterRef('year'),
            created_at__month=models.OuterRef('month'),
            created_at__week_day__in=[7, 1]
        ).values_list(
            models.Func('lines__gross_amount', function='SUM'),
        )

        return self.annotate(
            weekend_sales=models.Subquery(subquery),
        )
