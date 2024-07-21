from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from .models import Coupon


@admin.action(description="Activate Selected Coupon")
def activate_coupon(modelAdmin,request,queryset):
    queryset.update(active=True)
@admin.action(description="Deactivate Selected Coupon")
def deactivate_coupon(modelAdmin,request,queryset):
    queryset.update(active=False)

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    actions=[activate_coupon,deactivate_coupon]
    list_display=['code',
                  'valid_from',
                  'valid_to',
                  'discount_amount',
                  'active' ,'shop']
    list_editable=['discount_amount','shop']
    def get_queryset(self, request):
        qs=super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        
        return qs.filter(shop__owner=request.user)
    
    
    

# Register your models here.
