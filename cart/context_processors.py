from .cart import Cart
from coupons.models import Coupon
from django.utils import timezone




def cart(request):
    cart=Cart(request)
    now=timezone.now()
    try:
        coupon=Coupon.objects.get(valid_from__lte=now,valid_to__gte=now,active=True)
    except Coupon.DoesNotExist:
        coupon= None


    return {'cart':cart,
            'total_items':len(cart),
            'get_coupon_object':coupon}



