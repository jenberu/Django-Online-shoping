from .models import Shop

def shop(request):
    return {'shops':Shop()}