from django.shortcuts import render
from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem

def order_create(request):
    cart=Cart(request)
    if request.method=='POST':
        form=OrderCreateForm(request.POST)
        if form.is_valid():
            order=form.save()
            for item in cart:# this intract with cart __iter_ method it calls like cart.__iter__()
                OrderItem.objects.create(
                               order=order,
                               product=item['product'],
                               price=item['price'],
                               quantity=item['quantity']
                                         )
            cart.clear()
            return render(request,'orders/order/created.html', {'order': order})
    else:
        form=OrderCreateForm()
        return render(request,'orders/order/create.html',{'cart':cart,'form':form})

