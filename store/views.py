from django.shortcuts import render,get_object_or_404
from.models import Product,Category

# Create your views here.

def category_detail(request,slug):
    categroy = get_object_or_404(Category , slug=slug)
    products = categroy.products.all()
    return render(request,"store/category_detail.html",{'category':categroy,'products':products})

def product_details(request,category_slug, slug):
    product =get_object_or_404( Product,slug=slug)
    context = {"product":product}
    return render(request,"store/product_detail.html",context)
