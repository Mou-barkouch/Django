from django.shortcuts import render
from .models import Product 

# Create your views here.

def product(request):
    return render(request, 'products/product.html')

def products(request):
    return render(request, 'products/products.html',{'pro':Product.objects.all()})
### Product.objects.filter(price=12)
### Product.objects.order_by(price)
### srt(Product.objects.all().count())
### Product.objects.exclude(price=10)