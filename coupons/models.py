from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from shop.models import Shop

# models
class Coupon(models.Model):
    code=models.CharField(max_length=100,unique=True)
    valid_from=models.DateTimeField()
    valid_to=models.DateTimeField()
    discount_amount=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],help_text='percentage value (0 to 100)')
    active=models.BooleanField()
    shop=models.ForeignKey(Shop,related_name='couponshop',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.code
