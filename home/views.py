from django.shortcuts import render

# Create your views here.
from shop.models import Category, Product


def home(request, category_id=None):
    categories = Category.objects.all()
    products = Product.objects.all()

    context = {
        'categories': categories,
        'products': products,
    }

    return render(request, 'home/home.html',context)
