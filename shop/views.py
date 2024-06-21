from django.shortcuts import render , get_object_or_404,redirect
from .models import Product,Category,SubCategory
from cart.forms import CartAddProductForm
from .forms import ShopForm
from django.contrib.auth.models import User,Group
from django.urls import reverse
from django.db import IntegrityError



def product_list(request,category_slug=None,subcategory_slug=None):
    category=None
    subcategory = None
    searchedProduct=request.GET.get('searchProduct')
    categories=Category.objects.all()
    if searchedProduct:
            products=Product.objects.filter(available=True ,name__icontains=searchedProduct)
            if products:
                
                 return render(request,'shop/product/list.html',{'category':category,'categories':categories,'products':products,'search':searchedProduct}) 
            else:
                 return render(request,'shop/product/list.html',{'category':category,'categories':categories,'products':products,'search':searchedProduct,'noproduct':f'There is no  {searchedProduct}  product in our shop'})
    else:
        products=Product.objects.filter(available=True)
    
    
    if category_slug:
        category=get_object_or_404(Category,slug=category_slug)
        products=products.filter(category=category)
    if subcategory_slug:
         subcategory=get_object_or_404(SubCategory,slug=subcategory_slug)
         products=products.filter(subcategory=subcategory)
     
    return render(request,'shop/product/list.html',{'category':category,'categories':categories,'products':products}) 

def product_detail(request,id,slug):
    product=get_object_or_404(Product,id=id,slug=slug,available=True) 
    cart_product_form = CartAddProductForm()

    return render(request,'shop/product/detail.html',{'product':product,'cart_product_form':cart_product_form})

def add_shop(request):
     if request.method=='GET':
          form=ShopForm()
          return render(request,'shop/shops/shopform.html',{'form':form})
     else:
          form=ShopForm(request.POST)
          
          if form.is_valid():
               try:
                    onwer=get_object_or_404(User,username=request.user.username)

                    shop= form.save(commit=False)
                    shop.owner=onwer
                    shop.save()
               except IntegrityError:
                                 return render(request,'shop/shops/shopform.html',{'form':form,'error':'one onwer should register for one shop'})


               group, created = Group.objects.get_or_create(name='shoponwer')
               onwer.groups.add(group)
               return redirect('/admin/')

          else:
             return render(request,'shop/shops/shopform.html',{'form':form,'error':'please enter correct data'})





          




# Create your views here.
