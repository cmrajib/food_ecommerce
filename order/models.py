from django.conf import settings
from django.db import models

# Create your models here.
from UserRegistration.models import User, Coupon
from shop.models import Product






class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='cart')
    item = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __int__(self):
        return ((self.quantity) * (self.item))

    def get_total(self):
        total = self.item.price * self.quantity
        float_total = format(total, '0.2f')
        return float_total


class Order(models.Model):
    orderitems = models.ManyToManyField(Cart)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coupon = models.CharField(max_length=15,default=0)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    paymentId = models.CharField(max_length=264, blank=True, null=True)
    orderId = models.CharField(max_length=200, blank=True, null=True)

    def get_totals(self):
        total = 0
        for order_item in self.orderitems.all():
            total += float(order_item.get_total())
        return total

    def get_totals_with_coupon(self):
        total = 0
        for order_item in self.orderitems.all():
            total += float(order_item.get_total())
        total = total - float(self.user.coupon.amount)
        return total