from decimal import Decimal
from django.conf import settings
from shop.models import Product,Shop
from coupons.models import Coupon
from django.shortcuts import redirect

# Cart class to manage the cart
class Cart:
    def __init__(self,request):

         #note the  session data is stored as a dictionary
         #access the session using request.session
        self.session=request.session
        #The get() method returns the value for a key of dictionary if it exists, otherwise it returns None 
        cart=self.session.get(settings.CART_SESSION_ID)
        self.shop=self.session.get(settings.SHOP_SESSION_ID)

        if not cart:
            #save an empty cart in the ssesion
            cart=self.session[settings.CART_SESSION_ID]={}
        self.cart=cart 
        if not self.shop:
            self.shop = {}
            self.session[settings.SHOP_SESSION_ID] = self.shop

        
        self.coupon_id=self.session.get('coupon_id')
    def add(self,product,quantity=1,override_quantity=False):
        
        #add product to the cart or update its quantity

        """ convert the product ID into a 
           string because Django uses 
         JSON to serialize session data, 
         and JSON only allows string key names."""
        product_id=str(product.id)
        product_shop = product.shop.shopName
        if 'shopname' not in self.shop:
            self.shop['shopname'] = product_shop
            self.session[settings.SHOP_SESSION_ID] = self.shop

        if self.shop['shopname']==product_shop:
            if product_id not in self.cart:
            # assign the nested dectionary for cart[product_id] key
               self.cart[product_id]={
                'quantity':0,
                'price':str(product.price)
               }       
            if override_quantity:
                self.cart[product_id]['quantity'] = quantity #it is nested dictionary
            else:
                self.cart[product_id]['quantity']+=quantity
            self.save()
            return True
        else:
            return False
        

            print('you are allowed to use a cart for only one shop')      
    def save(self):
        self.session.modified=True  

    def remove(self,product):
        product_id=str(product.id)
        if product_id in self.cart:
            del self.cart[product_id] 
            self.save()  


    def __iter__(self):   # this is a built-in method in Python that is used to define an iterable object
         """ 
         the __iter__(self) method in a class is useful when you want to define 
         how instances of that class should be iterated over
  
 """
         product_ids=self.cart.keys()
         products=Product.objects.filter(id__in=product_ids)
         cart=self.cart.copy()
         for product in products:
             cart[str(product.id)]['product']=product
         for item in cart.values():
             item['price']=Decimal(item['price'])
             item['total_price']=item['price']*item['quantity']
             yield item # making it possible to iterate over the cart items directly   
    def __len__(self):
        return sum(item['quantity'] for  item in self.cart.values())
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    #clear the cart session
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        del self.session[settings.SHOP_SESSION_ID]

        self.save()
    @property
    def coupon(self):
        if self.coupon_id:
            try:
                return Coupon.objects.get(id=self.coupon_id)
            except Coupon.DoesNotExist:
                pass
        return None
    @property
    def get_shop(self):
        if self.shop:
            try:
                return Shop.objects.get(shopName=self.shop['shopname'])
            except Shop.DoesNotExist:
                pass
    
    
    def get_discount(self):
        if self.coupon:
            return(self.coupon.discount_amount/Decimal(100))*self.get_total_price()        
        return Decimal(0)
    def get_total_price_after_discount(self):
        return self.get_total_price() - self.get_discount()
