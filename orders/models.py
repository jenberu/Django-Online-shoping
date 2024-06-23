from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator,MaxValueValidator
from coupons.models import Coupon
from shop.models import Shop



class Order(models.Model):
    STATUS_CHOICE=[('pending','Pending'),
                   ('delivered','Delivered'),
                   ('out of delivery','Out of Delivery'),
                   ('confirmed','Order Confirmed'),
                   ]
    coupon=models.ForeignKey(Coupon,related_name='orders',null=True,blank=True,on_delete=models.SET_NULL)
    dicount=models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)])
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    address=models.CharField(max_length=100)
    postal_code=models.CharField(max_length=20)
    city=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    paid=models.BooleanField(default=False)
    status=models.CharField(max_length=30,choices=STATUS_CHOICE,default='Pending')
    shop=models.ForeignKey(Shop,on_delete=models.CASCADE,related_name='shop',null=True,blank=True)


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



class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey('shop.Product',related_name='order_items',on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.PositiveIntegerField(default=1)
    def __str__(self):
        return str(self.id)
    def get_cost(self):
        return self.price*self.quantity
