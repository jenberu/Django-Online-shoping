from django.urls import path
from . import views

app_name='shop'

urlpatterns=[
    path('',views.product_list,name='product_list'),
    path('subcategory/<slug:subcategory_slug>/',views.product_list,name='product_list_by_subcategory'),

    path('category/<slug:category_slug>/',views.product_list,name='product_list_by_category'),
    path('products/<int:shop_id>/',views.product_list,name='product_list_for_shop'),
    path('<int:id>/<slug:slug>/',views.product_detail,name='product_detail'),
    path('addshop/',views.add_shop,name='add_shop'),
    path('activate_shop/<int:shop_id>/',views.activate_shop,name='activate_shop'),
    path('shopadmin/',views.product_list_for_shop_owner,name='adminhome'),
    path('delete_product/<int:product_id>',views.delete_product,name='delete_product'),
    #path('products/<int:shop_id>',views.product_list_for_shop,name='product_list_for_shop'),
    



]