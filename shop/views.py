from decimal import Decimal

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# Create your views here.
from shop.models import Product, Category


def product(request, category_id=None):
    products = Product.objects.filter(discountprice__lte=0.0)
    latestproduct = Product.objects.all().order_by('DateArrived').filter(discountprice__lte=0.0)[:3]
    discountproduct = Product.objects.filter(discountprice__gte=0.1)

    categories = Category.objects.all()


    # search by category
    category=None
    if category_id:
        products = Product.objects.filter(category=category_id)
        category= Category.objects.get(id=category_id)



    # search by name
    search = ''
    if 'search' in request.GET:
        search = request.GET['search']
        if search:
            products = products.filter(title__icontains=search)






    # pagination
    paginator = Paginator(products, 2)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)

    context = {
        'products': paged_product,
        'discountproduct': discountproduct,
        'latestproduct': latestproduct,
        'search': search,
        'categories': categories,
        'category': category,
    }

    return render(request, 'shop/product.html', context)


def productdetail(request, id):

    product = Product.objects.get(id=id)
    print(product)

    context = {
        'product': product,
    }


    return render(request,'shop/productdetail.html', context)
