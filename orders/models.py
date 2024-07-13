from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator,MaxValueValidator
from coupons.models import Coupon
from shop.models import Shop
from django.conf import settings
from django.utils.translation import gettext_lazy as _





class Order(models.Model):
    STATUS_CHOICE=[('pending','Pending'),
                   ('delivered','Delivered'),
                   ('out of delivery','Out of Delivery'),
                   ('confirmed','Order Confirmed'),
                   ]
    coupon=models.ForeignKey(Coupon,related_name='orders',null=True,blank=True,on_delete=models.SET_NULL)
    dicount=models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)])
    #u can pass the verbose_name as the first positional argument
    first_name=models.CharField('first name',max_length=50,)
    last_name=models.CharField(_('last name'),max_length=50)
    email=models.EmailField(_('e-mail'))
    address=models.CharField(_('address'),max_length=100)
    postal_code=models.CharField(_('postal_code'),max_length=20)
    city=models.CharField(_('city'),max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    paid=models.BooleanField(default=False)
    status=models.CharField(max_length=30,choices=STATUS_CHOICE,default=STATUS_CHOICE[0])
    shop=models.ForeignKey(Shop,on_delete=models.CASCADE,related_name='shop',null=True,blank=True)
    stripe_id=models.CharField(max_length=250,blank=True)


    class Meta:
        ordering = ['-created']
        indexes = [models.Index(fields=['-created']),]

    def __str__(self):
        return f'Order {self.id}'
    def get_total_cost(self):
        return self.get_total_cost_before_discount() -self.get_discount()
    def get_total_cost_before_discount(self):
        return sum(item.get_cost() for item in self.items.all())
    def get_discount(self):
        total_cost=self.get_total_cost_before_discount()
        if self.dicount:
            return (self.dicount/Decimal(100))*total_cost
        return Decimal(0)
    # method to return the Stripe dashboard’s URL
    def get_stripe_url(self):
        if not self.stripe_id:
            return ''
        #differtient the production environment from the test environment.
        if '_test_' in settings.STRIPE_SECRET_KEY:
            path='/test/'
        else:
            path='/'
        return f'https://dashboard.stripe.com{path}payments/{self.stripe_id}'       



class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey('shop.Product',related_name='order_items',on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.PositiveIntegerField(default=1)
    def __str__(self):
        return str(self.id)
    def get_cost(self):
        return self.price*self.quantity
