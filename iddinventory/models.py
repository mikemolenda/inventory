from django.db import models


class Product(models.Model):
    manufacturer = models.CharField(max_length=200)
    model_no = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='../images/items', blank=True, null=True)


class Asset(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)



