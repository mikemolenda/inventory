from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    manufacturer = models.CharField(max_length=100)
    model_no = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='../images/items', blank=True, null=True)


class Asset(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT, blank=True, null=True)
    vendor_item_no = models.CharField(max_length=100, blank=True, null=True)
    acquire_date = models.DateField(blank=True, null=True)
    purchase_price = models.DecimalField(max_length=8, decimal_places=2, blank=True, null=True)
    serial_no = models.CharField(max_length=100, blank=True, null=True)
    asset_tag_no = models.CharField(max_length=100, blank=True, null=True)
    capital_equipment = models.BooleanField()
    storage_location = models.CharField(max_length=200, blank=True, null=True)
    comments = models.CharField(max_length=400, blank=True, null=True)


class Category(models.Model):
    label = models.CharField(max_length=100)


class AssetCategory(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

