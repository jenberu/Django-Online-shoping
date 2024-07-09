
from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from shop.models import Product
admin.site.site_header='Shop Admin'
admin.site.index_title="Admin"
admin.site.empty_value_display="None"



urlpatterns = [
    path('admin/', admin.site.urls ,name='admin'),
    path('cart/', include('cart.urls', namespace='cart')),
    path('oredrs/',include('orders.urls',namespace='orders')),
     path('coupons/', include('coupons.urls', namespace='coupons')),
     path('payment/', include('payment.urls', namespace='payment')),

    path('',include('shop.urls',namespace='shop')),
    path('accounts/', include('accounts.urls')),
    path('news/',include('news.urls')),



]

if settings.DEBUG:
 urlpatterns += static(
 settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
 )
