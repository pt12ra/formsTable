from django.db import models

class Act(models.Model):
    institution = models.CharField(max_length=200)
    date1 = models.DateField('Act confirm date')
    order_number = models.IntegerField
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.act_text

class Member(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)

    def __str__(self):
        return self.member_text

class Product(models.Model):
    nr = models.IntegerField
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.product_text

    def calc_price(self):
        return self.total / self.quantity

class Seller:
    name = models.CharField(max_length=200)
    serial = models.CharField(max_length=200)
    number = models.IntegerField
    date = models.DateField('Act confirm date')

    def __str__(self):
        return self.seller_text


