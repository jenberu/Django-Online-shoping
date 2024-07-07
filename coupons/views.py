from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from django.utils import timezone
from .forms import CouponForm
from .models import Coupon
from django.contrib import messages


@require_POST
def apply_coupon(request):
    now=timezone.now()
    form=CouponForm(request.POST)

    if form.is_valid():
        code=form.cleaned_data['code']

        try:
            coupon=Coupon.objects.get(code__iexact=code,valid_from__lte=now,valid_to__gte=now,active=True)

            request.session['coupon_id']=coupon.id
        except Coupon.DoesNotExist:

            request.session['coupon_id']=None

    return redirect('cart:cart_detail')            


# Create your views here.
