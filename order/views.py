from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from UserRegistration.models import Coupon, User
from order.models import Cart, Order
from shop.models import Product

login_required
def add_to_cart(request, pk):
    if request.user.is_authenticated:
        item = get_object_or_404(Product, pk=pk)
        order_item = Cart.objects.get_or_create(item=item, user=request.user, purchased=False)
        order_qs = Order.objects.filter(user=request.user, ordered=False)
        if order_qs.exists():
            order = order_qs[0]
            if order.orderitems.filter(item=item).exists():
                order_item[0].quantity += 1
                order_item[0].save()
                # messages.info(request, "This item quantity is updated")
                return redirect("home:home")
            else:
                order.orderitems.add(order_item[0])
                messages.info(request, "This item is addedd to your cart")
                return redirect("home:home")
        else:
            order = Order(user=request.user)
            order.save()
            order.orderitems.add(order_item[0])
            messages.info(request, "This item is added to your cart")
            return redirect("home:home")
    else:
        return redirect('UserRegistration:login')


@login_required
def cart_view(request):
    coupon = False

    couponData = Coupon.objects.filter(user=request.user, transaction=False)
    couponId = None
    if request.method == 'POST':
        couponId = request.POST['coupon']
        # couponData = Coupon.objects.filter(user=request.user, couponId=couponId)

        couponData =  Coupon.objects.filter(user=request.user, transaction=False)
        couponupdate = Coupon.objects.get(user=request.user)
        if couponData:
            coupon = True
            couponupdate.transaction = True
            couponupdate.save()
        else:
            coupon = False
            couponupdate.transaction = False
            couponupdate.save()
        couponData = Coupon.objects.filter(user=request.user)

    carts = Cart.objects.filter(user=request.user, purchased=False).distinct()
    orders = Order.objects.filter(user=request.user, ordered=False).distinct()

    if carts.exists() and orders.exists():
        order = orders[0]

        context = {
            'carts': carts,
            'order': order,
            'coupon': coupon,
            'couponId': couponId,
            'couponData': couponData,
        }


        return render(request, 'order/cart.html', context)
    else:
        # messages.warning(request, "You don't have any item in your cart")
        return redirect("home:home")


@login_required
def remove_from_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            order.orderitems.remove(order_item)
            order_item.delete()
            # messages.warning(request, "This item was removed form your cart")
            return redirect("order:cart")
        else:
            # messages.info(request, "This item was not in your cart")
            return redirect("home:home")
    else:
        # messages.info(request,"You don't have an active order")
        return redirect("home:home")

@login_required
def increase_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            if order_item.quantity >= 1:
                order_item.quantity += 1
                order_item.save()
                # messages.info(request, f"{item.name} quantity has been updated")
                return redirect("order:cart")
            else:
                # messages.info(request, f"{item.name} in not in your cart")
                return redirect("home:home")
        else:
            # messages.info(request, "You don't have an active order")
            return redirect("hom:home")

@login_required
def decrease_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                # messages.info(request, f"{item.name} quantity has been updated")
                return redirect("order:cart")
            else:
                order.orderitems.remove(order_item)
                order_item.delete()
                # messages.warning(request, f"{item.name} item has been removed form your cart")
                return redirect("order:cart")
        else:
            # messages.info(request, "You don't have an active order")
            return redirect("home:home")


