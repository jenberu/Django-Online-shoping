from django.contrib import admin
from .models import Coupon

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display=['code',
                  'valid_from',
                  'valid_to',
                  'discount_amount',
                  'active' ]
    list_editable=['discount_amount']
    

# Register your models here.
