from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from.models import Userprofile
from store.forms import ProductForm,Product
from store.models import Category
from django.utils.text import slugify
from django.contrib import messages

# Create your views here.
def vendor_details(request,pk):
    user=User.objects.get(pk=pk)
    products = user.products.filter(status=Product.ACTIVE)
    return render(request,"userprofile/vendor_detail.html",context={'user':user,'products':products})

@login_required
def mystore(request):
    products = request.user.products.exclude(status=Product.DELETED)
    return render(request,"userprofile/mystore.html",{'products':products})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            title = request.POST.get('title')   
            product = form.save(commit=False)
            product.user = request.user
            product.slug = slugify(title)
            product.save()
            messages.success(request,'The Product was added!')
            return redirect("mystore")   
    else:
        form = ProductForm()
    return render(request,"userprofile/product_form.html",{'title':'Add Product','form':form})

@login_required
def edit_product(request,pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES,instance=product)
    
        if form.is_valid():
            form.save()
            messages.success(request,"The changes was saved!")
            return redirect("mystore")   
    else: 
        form = ProductForm(instance=product)
    return render(request,"userprofile/product_form.html",{'title':'Edit Product','product':product,'form':form})

@login_required
def delete_product(request,pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    product.status=Product.DELETED
    product.save()
    messages.success(request,"The Product was deleted!")
    return redirect('mystore')

@login_required
def myaccount(request):
    return render(request,'userprofile/myaccount.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            userprofile = Userprofile.objects.create(user=user)
            return redirect("frontpage")
    else:
        form = UserCreationForm()
    return render(request,"userprofile/signup.html",{'form':form})
            