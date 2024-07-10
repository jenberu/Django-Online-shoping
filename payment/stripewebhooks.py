import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order
from shop.models import Product
from shop.recommender import Recommander


@csrf_exempt
def stripe_webhook(request):
    payload=request.body# ths get the body of request as string
    # META atribute  of request is used to get the header information of request
    sig_header=request.META['HTTP_STRIPE_SIGNATURE']
    event=None
    try:
        event=stripe.Webhook.construct_event(
            payload,sig_header,settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # for invalid payload return an HTTP 400 Bad Request response
        return HttpResponse(status=400) 
    except stripe.error.SignatureVerificationError as e:
        # for invalide ID signature return an HTTP 400 Bad Request response
        return HttpResponse(status=400)
    if event.type=='checkout.session.completed':
        session=event.data.object
        if(session.mode=='payment' and session.payment_status=='paid'):
            try:
                order=Order.objects.get(id=session.client_reference_id)
            except Order.DoesNotExist:
                return HttpResponse(status=404) 
            #store the payment intent id to  stripe_id field of the Order object
            order.stripe_id=session.payment_intent
            order.paid=True
            order.save()   
            #store the purchased product to ProductRecommendation model
            product_ids=order.items.values_list('product_id',flat=True)
            recommender=Recommander()
            recommender.products_bought(product_ids)
    #else retturn HTTP 200 ok response
    return HttpResponse(status=200) 
    

