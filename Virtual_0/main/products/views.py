from django.shortcuts import render
from .models import Product 

# Create your views here.

def product(request):
    return render(request, 'products/product.html')

def products(request):
    return render(request, 'products/products.html',{'pro':Product.objects.all()})
### Product.objects.filter(price=12)
### Product.objects.filter(price__exect=12)
### Product.objects.filter(name__contains='a')
### Product.objects.filter(price__in=[1,30,6])
### Product.objects.filter(price__range=[1,30])
### Product.objects.order_by(price)
### srt(Product.objects.all().count())
### Product.objects.exclude(price=10)