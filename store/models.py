from django.db import models
from jsonfield import JSONField


class Product(models.Model):
    """
        Model to store product detail
    """
    product_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=1023)
    body_html = models.CharField(max_length=1023)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    variants = JSONField()
    options = JSONField()
    images = JSONField()
    image = JSONField()

    def __str__(self):
        return "{}: {}".format(self.product_id, self.title)


class Order(models.Model):
    """
        Model to store order details
    """
    order_id = models.IntegerField(unique=True)
    user_email = models.CharField(max_length=1023, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    total_price = models.FloatField()
    order_number = models.IntegerField()
    line_items = JSONField()

    def __str__(self):
        return "#{}".format(self.order_number)
