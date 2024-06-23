from .models import Shop

def shop(request):
    return {'shop':Shop()}