from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# models
class Coupon(models.Model):
    code=models.CharField(max_length=100,unique=True)
    valid_from=models.DateTimeField()
    valid_to=models.DateTimeField()
    dicount_amount=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],help_text='percentage value (0 to 100)')
    active=models.BooleanField()
    def __str__(self):
        return self.code
