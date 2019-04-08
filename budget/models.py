from django.db import models

from .managers import MonthlyBudgetQuerySet


class SalesTarget(models.Model):

    year = models.IntegerField()
    month = models.IntegerField()
    target = models.DecimalField(max_digits=10, decimal_places=2)

    objects = MonthlyBudgetQuerySet.as_manager()

    class Meta:
        # We can only have one budget for a month
        unique_together = (('year', 'month'), )

        # Month can only be 1 through 12
        constraints = [
            models.CheckConstraint(
                check=models.Q(month__in=range(1, 13)),
                name='check_valid_month'
            ),
        ]
