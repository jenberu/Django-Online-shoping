from django.urls import path
from . import views

app_name='shop'

urlpatterns=[
    path('',views.product_list,name='product_list'),
    path('subcategory/<slug:subcategory_slug>/',views.product_list,name='product_list_by_subcategory'),

    path('category/<slug:category_slug>/',views.product_list,name='product_list_by_category'),
    path('<int:id>/<slug:slug>/',views.product_detail,name='product_detail'),
    path('addshop/',views.add_shop,name='add_shop'),
    path('shopadmin/',views.product_list_for_shop_owner,name='adminhome'),


]