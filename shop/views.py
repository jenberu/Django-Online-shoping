from django.shortcuts import render , get_object_or_404
from .models import Product,Category,SubCategory
from cart.forms import CartAddProductForm

def product_list(request,category_slug=None,subcategory_slug=None):
    category=None
    subcategory = None
    searchedProduct=request.GET.get('searchProduct')
    categories=Category.objects.all()
    if searchedProduct:
            products=Product.objects.filter(available=True ,name__icontains=searchedProduct)
            if products:
                
                 return render(request,'shop/product/list.html',{'category':category,'categories':categories,'products':products}) 
            else:
                 return render(request,'shop/product/list.html',{'category':category,'categories':categories,'products':products,'noproduct':'there is no such product in our shop'})
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




# Create your views here.
