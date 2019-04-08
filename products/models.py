from django.db import models, transaction


class Product(models.Model):

    name = models.CharField(max_length=1024)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    inventory = models.PositiveIntegerField()

    def purchase(self):

        with transaction.atomic():

            # We select the product again from the database, to ensure we have
            # the latest version and we select it for update to ensure no one
            # else can update the object while we modify it.
            product = Product.objects.select_for_update().get(pk=self.pk)

            # Check that we have at least one product in inventory. This is
            # guaranteed to be correct because we have a lock on the row.
            if product.inventory < 1:
                raise ValueError('Inventory of %s is empty', product.name)

            product.inventory -= 1
            product.save()
