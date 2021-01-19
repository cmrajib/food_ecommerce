from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from UserRegistration.models import Coupon
from order.models import Order
from payment.models import BillingAddress



@login_required
def checkout(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            address1 = request.POST['address1']
            address2 = request.POST['address2']
            zipcode = request.POST['zipcode']
            city = request.POST['city']
            state = request.POST['state']
            country = request.POST['country']
            phone = request.POST['phone']

            BillingAddress.objects.create(first_name=first_name, last_name=last_name,
                                            address1=address1, address2=address2,
                                                      zipcode=zipcode,city=city,state=state,
                                                      country=country,phone=phone)
            BillingAddress.save()


    couponData = Coupon.objects.filter(user=request.user, transaction=True)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order_items = order_qs[0].orderitems.all()
    subtotal = order_qs[0].get_totals()
    if not couponData:
        order_total = order_qs[0].get_totals()
    else:
        order_total = order_qs[0].get_totals_with_coupon()

    couponAmount = Coupon.objects.all().filter(user=request.user)

    context = {
        'order_items': order_items,
        'order_total': order_total,
        'couponData': couponData,
        'subtotal': subtotal,
    }


    return render(request, 'payment/checkout.html',context)
