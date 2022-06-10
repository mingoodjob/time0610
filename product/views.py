from django.shortcuts import render
from django.http import HttpResponse
from product.models import Category, UserOrder, OrderStatus,Product

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})

def new_order(request, id):
    product = Product.objects.get(id=id)
    print(product.title)
    return HttpResponse(product.title)
