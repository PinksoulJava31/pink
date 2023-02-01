from django.db import models


# Create your models here.
class product(models.Model):
    product_name=models.CharField(max_length=25)
    product_price=models.IntegerField()
    product_quantity=models.IntegerField()
    def _str_(self):
        return self.product_name

       