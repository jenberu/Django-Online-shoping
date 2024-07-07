from django.shortcuts import render , get_object_or_404,redirect
from .models import Product,Category,SubCategory,Shop
from cart.forms import CartAddProductForm
from .forms import ShopForm
from django.contrib.auth.models import User,Group
from django.urls import reverse
from django.db import IntegrityError
from django.contrib import messages
from orders.models import OrderItem,Order



def product_list(request,shop_id=None,category_slug=None,subcategory_slug=None):
    category=None
    subcategory = None
    searchedProduct=request.GET.get('searchProduct')
    categories=Category.objects.all()
    shops=Shop.objects.filter(is_active=True)
    if searchedProduct:
            products=Product.objects.filter(available=True ,name__icontains=searchedProduct)
            if products:
                
                 return render(request,'shop/product/list.html',{'category':category,'categories':categories,'products':products,'search':searchedProduct,'shops':shops}) 
            else:
                 return render(request,'shop/product/list.html',{'category':category,'categories':categories,'products':products,'search':searchedProduct,'shops':shops,'noproduct':f'There is no  {searchedProduct}  product in our shop'})
    else:
        products=Product.objects.filter(available=True)
    
    
    if category_slug:
        category=get_object_or_404(Category,slug=category_slug)
        products=products.filter(category=category)
    if subcategory_slug:
         subcategory=get_object_or_404(SubCategory,slug=subcategory_slug)
         products=products.filter(subcategory=subcategory)
    if shop_id:
          shop = get_object_or_404(Shop, id=shop_id)
          products=products.filter(shop=shop,available=True)    
     
    return render(request,'shop/product/list.html',{'category':category,'categories':categories,'products':products,'shops':shops}) 

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
                    request.session['shop_id']=shop.id
                    return redirect('payment:onwer_payment_procces')
                    
                   

               except IntegrityError:
                                 return render(request,'shop/shops/shopform.html',{'form':form,'error':'one onwer should register for one shop'})



          else:
             return render(request,'shop/shops/shopform.html',{'form':form,'error':'please enter correct data'})
def product_list_for_shop_owner(request):
      user=get_object_or_404(User,username=request.user.username)
      shop=Shop.objects.get(owner=user,is_active=True)
      products=Product.objects.filter(available=True,shop=shop)
      return render(request,'shop/shops/adminpage.html',{'products':products}) 
def delete_product(request,product_id):
       product=Product.objects.get(id=product_id)
       if product !=None:
             product.delete()
             messages.success(request, 'Product deleted successfully')

       return redirect('/adminhome/')
def product_list_for_shop(request,shop_id,category_slug=None,subcategory_slug=None):
      shop = get_object_or_404(Shop, id=shop_id)
      products=Product.objects.filter(shop=shop,available=True)
      return render(request,'shop/product/list.html',{'products':products}) 


      
          



      

      




          




# Create your views here.
