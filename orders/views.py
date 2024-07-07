from django.shortcuts import render,get_object_or_404,redirect
from cart.cart import Cart
from .forms import OrderCreateForm, UpdateStatusForm
from .models import OrderItem ,Order
from  django.contrib.admin.views.decorators import staff_member_required
import weasyprint
from django.contrib.staticfiles import finders
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db import IntegrityError


def order_create(request):
    cart=Cart(request)
    if request.method=='POST':
        form=OrderCreateForm(request.POST)
       
        if form.is_valid():
                order=form.save(commit=False)
                if cart.get_shop:
                    order.shop=cart.get_shop
                if cart.coupon:
                    order.coupon=cart.coupon
                    order.dicount=cart.coupon.discount_amount
                order.save()
                for item in cart:# this intract with cart __iter_ method it calls like cart.__iter__()
                    OrderItem.objects.create(
                               order=order,
                               product=item['product'],
                               price=item['price'],
                               quantity=item['quantity']
                                         )
                cart.clear()
                request.session['order_id']=order.id
                return redirect('payment:paymentprocces')
               # return render(request,'orders/order/created.html', {'order': order})
        else:
            return render(request, 'orders/order/create.html', {'form':OrderCreateForm, 'error':'please enter valid data  for all fields'})
           
    else:
        total_items = len(cart)
        if total_items==0:  
            return render(request,'cart/detail.html',{'error':'your cart is empity pleace add item to checkout'})

        form=OrderCreateForm()
        return render(request,'orders/order/create.html',{'cart':cart,'form':form})
@staff_member_required
def admin_order_detail(request,order_id):
    order=get_object_or_404(Order,id=order_id)
    return  render(request, 'admin/orders/order/admindetail.html', {'order': order})   
@staff_member_required
def admin_order_pdf(request,order_id):
    order=get_object_or_404(Order,id=order_id)
    html=render_to_string('orders/order/pdf.html', {'order': order})
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']=f'filename=order_{order.id}.pdf'# specifay the file name
    weasyprint.HTML(string=html).write_pdf(response,stylesheets=[weasyprint.CSS(finders.find('css/pdf.css'))])
    return response

def updateStatus(request,order_id):
    order=get_object_or_404(Order,id=order_id)

    if request.method =='GET':
        form=UpdateStatusForm()
        return render(request,'orders/order/updateorderstatus.html',{'form':form,'order':order})
    else:
        form=UpdateStatusForm(request.POST)

        if form.is_valid():
            order.status=form.cleaned_data['status']
            order.save()
            return redirect('/admin/orders/order/') 



