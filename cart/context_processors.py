from .cart import Cart



def cart(request):
    cart=Cart(request)
    return {'cart':cart,
            'total_items':len(cart)}


