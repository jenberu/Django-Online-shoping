from django.shortcuts import render, get_object_or_404,redirect

from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import  login_required
from shop.models import Product,Shop
from .cart import Cart
from .forms import CartAddProductForm
from coupons.forms import CouponForm
from coupons.models import Coupon
from shop.recommender import Recommender
from django.utils.translation import gettext_lazy as _



@login_required
@require_POST
def cart_add(request,product_id):
    #shop=get_object_or_404(Shop,shopName=shop_name)
    cart=Cart(request)
    product=get_object_or_404(Product,id=product_id)
    form=CartAddProductForm(request.POST)
    if form.is_valid():
        cd=form.cleaned_data
        is_add= cart.add(product=product,quantity=cd['quantity'],override_quantity=cd['override'])
        if is_add:
           return redirect('cart:cart_detail') 
        else:
            return render(request, 'cart/detail.html', {'cart': cart,'error':_('you should checkout this cart before requesting the order in other shop')})  

           
@require_POST
def cart_remove(request,product_id):
    cart=Cart(request)
    product=get_object_or_404(Product,id=product_id)
    cart.remove(product)
    if len(cart)==0:
       cart.clear()
       return redirect('shop:product_list')
    return redirect('cart:cart_detail') 

def cart_detail(request):
 cart = Cart(request)
 total_items = len(cart)
 if total_items==0:    
    cart.clear()
 for item in cart:
    item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'override': True} )
 coupon_apply_form= CouponForm() 
 recommended_products=None
 recommender=Recommender()
 products_in_cart=[item['product'] for item in cart]
 if products_in_cart:

    recommended_products=recommender.get_purchased_products(products_in_cart)
 if cart.get_shop:
    shop=cart.get_shop 
    try:
       coupon=Coupon.objects.filter(shop=shop)
       return render(request, 'cart/detail.html', {'cart': cart,'coupon':coupon,'coupon_apply_form':coupon_apply_form,'recommended_products':recommended_products})  
    except Coupon.DoesNotExist:
        return render(request, 'cart/detail.html', {'cart': cart,'coupon_apply_form':coupon_apply_form,'recommended_products':recommended_products})  
 return render(request, 'cart/detail.html', {'cart': cart,'coupon_apply_form':coupon_apply_form,'recommended_products':recommended_products})  







   
   
