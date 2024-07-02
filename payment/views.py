from django.shortcuts import render,get_object_or_404,redirect
import stripe
from django.conf import settings
from django.urls import reverse 
from orders.models import Order
from decimal import Decimal


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