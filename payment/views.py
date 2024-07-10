from django.shortcuts import render,get_object_or_404,redirect
import stripe
from django.conf import settings
from django.urls import reverse 
from orders.models import Order
from decimal import Decimal
from shop.models import Shop,ShopSubscrioptionPlan
from datetime import timedelta
from django.utils import timezone
from django.http import HttpResponse




stripe.api_key=settings.STRIPE_SECRET_KEY
stripe.api_version=settings.STRIPE_API_VERSION

def payment_procces(request):
    #get order_id from from stored session by order_create view
    order_id=request.session.get('order_id')
     #get order object by this id
    order=get_object_or_404(Order,id=order_id)
    if request.method=='POST':
        # generate an absolute URI from the URL path
        successurl=request.build_absolute_uri(reverse('payment:completed'))
        cancel_url=request.build_absolute_uri(reverse('payment:canceled'))
        #checkout session Data
        strip_session_data={
            'mode':'payment',
            'client_reference_id':order.id,
            'success_url':successurl,
            'cancel_url':cancel_url,
            'line_items':[] #A list of items the customer is purchasing
                  }
        for item in order.items.all():
            strip_session_data['line_items'].append(
                {
                    'price_data':{
                        'unit_amount':int(item.price * Decimal('100')),
                         'currency':'etb',#currency for Ethiopia
                         #: Product-related information:
                         'product_data':{
                             'name':item.product.name,#name of the product
                         },
                    },
                    'quantity':item.quantity,
                }
            )
        #adding Dicount info to  Stripe 
        if order.coupon:
             stripe_coupon=stripe.Coupon.create(name=order.coupon.code,
                                                percent_off=order.dicount,
                                                duration='once')
             # links the coupon to the checkout session
             strip_session_data['discounts']=[{'coupon':stripe_coupon.id}]


        #call strip Session.create() method to  create stripe checkout session
        # builds and sends the request to the Stripe API
        stripe_session=stripe.checkout.Session.create(**strip_session_data)
        #after creating the checkout session, an HTTP redirect with status code 303 is returned to redirect the user to Stripe page
        return redirect(stripe_session.url,code=303)#redirect to Stripe payment page using the URL from the session object
    else:
        return render(request,'payment/process.html',locals())
    

def payment_completed(request):
    return render(request, 'completed.html')
def payment_canceled(request):
    return render(request,'canceled.html')


#notes
"""303 status code (See Other) is used to indicate that the client(browser) should perform a GET request to the provided URL
Using locals() in the render function will include all local variables in the context passed to the template.
 This can be convenient but may also include unnecessary data. 
 It is often better to explicitly define the context variables you want to pass to the template for clarity and to avoid passing unintended data.

"""

def shop_onwer_payemnet_procces(request):
    #retrive shop_id from session
    shop_id=request.session.get('shop_id')
    shop=get_object_or_404(Shop,id=shop_id)
    try:
         sub_plan_per_month=ShopSubscrioptionPlan.objects.get(plan_name='monthly')
         sub_plan_per_six_month=ShopSubscrioptionPlan.objects.get(plan_name='six_months')
         sub_plan_per_six_year=ShopSubscrioptionPlan.objects.get(plan_name='yearly')
    except ShopSubscrioptionPlan.DoesNotExist:
         return render(request,'payment/onwer_process.html',{'error':"There is no  such Subscription"})
             

    if request.method=="POST":
        
        success_url = request.build_absolute_uri(reverse('payment:onwer_completed'))
        cancel_url = request.build_absolute_uri(reverse('payment:onwer_canceled'))
        plan=request.POST['plan']
        request.session['plan']=plan

        if plan=='monthly':
            shop_sub_plan=sub_plan_per_month
            price=int(shop_sub_plan.price * Decimal('100'))


        elif plan=='six_months':
            shop_sub_plan=sub_plan_per_six_month
            price=int(shop_sub_plan.price * Decimal('100'))
        elif plan=='yearly':
            shop_sub_plan=sub_plan_per_six_year
            price=int(shop_sub_plan.price * Decimal('100'))
        else:
             return HttpResponse("Invalid plan", status=400)
        session=stripe.checkout.Session.create(
              payment_method_types=['card'],
              line_items=[{
                   'price_data': {
                   'currency': 'etb',
                    'product_data': {
                    'name': f'{plan.capitalize()} Subscription for {shop.shopName}',
                      },
                   'unit_amount': price,
                    },
                 'quantity': 1,
                   }],
               mode='payment',
               success_url=success_url ,
               cancel_url=cancel_url,

               )
        return redirect(session.url,code=303)
        
    else:
        return render(request,'payment/onwer_process.html',{'sub_plan_per_month':sub_plan_per_month,'sub_plan_per_six_month':sub_plan_per_six_month,'sub_plan_per_six_year':sub_plan_per_six_year})


def onwer_payment_success(request):
    plan=request.session.get('plan')
    shop_id=request.session.get('shop_id')
     #get shop object by this id
    shop=get_object_or_404(Shop,id=shop_id)
    if plan=='monthly':
         duration=timedelta(days=30)
    elif plan=='six_months':
            duration=timedelta(days=180)
    elif plan=='yearly':
            duration=timedelta(days=365) 
    shop.activate_shop(duration)  
   

    return render(request, 'payment/onwer_success.html', {'shop': shop})

def onwer_payment_cancele(request):
      return render(request, 'payment/onwer_cancel.html')
     
 



