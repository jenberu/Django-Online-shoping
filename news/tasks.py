from .models import Advertisment
from django.utils import timezone

class Task:
    def deactivate_adds(self):
        now=timezone.now()
        expired_ads=Advertisment.objects.filter(end_date__lt=now,active=True)
        expired_ads.update(active=False)


