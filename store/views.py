from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q
from.models import Product,Category
from.cart import Cart


def add_to_cart(request,product_id):
    cart = Cart(request)
    cart.add(product_id)
    return redirect('frontpage')
    
def search(request):
    query = request.GET.get('query','')
    product = Product.objects.filter(status=Product.ACTIVE).filter(Q(title__icontains=query) | Q(description__icontains=query))
    
    return render(request,"store/search.html",{'query':query,'products':product})

def category_detail(request,slug):
    categroy = get_object_or_404(Category , slug=slug)
    products = categroy.products.filter(status=Product.ACTIVE)
    return render(request,"store/category_detail.html",{'category':categroy,'products':products})

def product_details(request,category_slug, slug):
    product =get_object_or_404( Product,slug=slug,status=Product.ACTIVE)
    context = {"product":product}
    return render(request,"store/product_detail.html",context)