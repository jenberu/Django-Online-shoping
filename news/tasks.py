from .models import Advertisment
from django.utils import timezone
from shop.models import Shop
class Task:
    now=timezone.now()
    def deactivate_adds(self):
        expired_ads=Advertisment.objects.filter(end_date__lt=self.now,active=True)
        expired_ads.update(active=False)
    def deactivate_shop(self):
        expired_shops=Shop.objects.filter(valid_to__lt=self.now,is_active=True)   
        expired_shops.update(is_active=False) 


