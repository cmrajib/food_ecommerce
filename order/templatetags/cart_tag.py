from django import template


from UserRegistration.models import Coupon
from order.models import Order

register = template.Library()

@register.filter
def cart_total(user):
    order = Order.objects.filter(user=user, ordered=False)

    if order.exists():
        return order[0].orderitems.count()
    else:
        return 0



@register.filter
def total_amount(user):
    order_qs = Order.objects.filter(user=user, ordered=False)
    coupon = Coupon.objects.filter(user=user, transaction=False)
    if coupon:
        return order_qs[0].get_totals()
    else:
        return order_qs[0].get_totals_with_coupon()


    # order_items = order_qs[0].orderitems.all()
    # order_total = order_qs[0].get_totals()
