from django.db import models



class Order(models.Model):
    STATUS_CHOICE=[('pending','Pending'),
                   ('delivered','Delivered'),
                   ('out of delivery','Out of Delivery'),
                   ('confirmed','Order Confirmed'),
                   ]
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


    class Meta:
        ordering = ['-created']
        indexes = [models.Index(fields=['-created']),]

    def __str__(self):
        return f'vOrder {self.id}'
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey('shop.Product',related_name='order_items',on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.PositiveIntegerField(default=1)
    def __str__(self):
        return str(self.id)
    def get_cost(self):
        return self.price*self.quantity
