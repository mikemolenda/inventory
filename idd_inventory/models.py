from django.db import models


class Vendor(models.Model):
    name = models.CharField()
    website = models.URLField(blank=True, null=True)
    comments = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField()
    website = models.URLField(blank=True, null=True)
    comments = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT)
    model_name = models.CharField()
    model_no = models.CharField(blank=True, null=True)
    image = models.ImageField(upload_to='../images/items', blank=True, null=True)
    support_website = models.URLField(blank=True, null=True)
    comments = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return str(self.manufacturer) + ' ' + self.model_name


class Asset(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT, blank=True, null=True)
    vendor_item_no = models.CharField(blank=True, null=True)
    acquire_date = models.DateField(blank=True, null=True)
    purchase_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    serial_no = models.CharField(blank=True, null=True)
    asset_tag_no = models.CharField(blank=True, null=True)
    capital_equipment = models.BooleanField()
    storage_location = models.CharField(blank=True, null=True)
    comments = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return str(self.product) + ' ' + str(self.id)


class Category(models.Model):
    label = models.CharField()

    def __str__(self):
        return self.label


class AssetCategory(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.asset) + ': ' + str(self.category)

