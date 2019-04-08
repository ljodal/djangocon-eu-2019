from django.db import models

from .managers import CustomerQuerySet


class Customer(models.Model):

    name = models.CharField(max_length=1024)

    objects = CustomerQuerySet.as_manager()
