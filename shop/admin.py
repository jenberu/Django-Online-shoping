from typing import Any
from django.contrib import admin
from .models import Category,Product,SubCategory,Shop,ShopSubscrioptionPlan,ProductRecommandation
from django.utils.html import mark_safe,format_html ,urlencode
from .forms import ProductAdminForm
from django.urls import reverse
from django.utils import timezone


admin.site.register(ShopSubscrioptionPlan)
admin.site.register(ProductRecommandation)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','product_count']
    prepopulated_fields={'slug':('name',)}
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(shop__owner=request.user)
    @admin.display(ordering='product_count')
    def product_count(self,category):
        #add url with admin:app_model_page format
        url=(reverse('admin:shop_product_changelist')
             + '?'
             +urlencode({
                 'category__id':category.id
             })
             )
        return format_html('<a href="{}">{}</a>',url, category.products.count())
        
    product_count.short_description = 'Number of Products'
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser:
            if db_field.name == 'shop':
                kwargs['queryset'] = Shop.objects.filter(owner=request.user)   
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display=['name','category','slug']
    prepopulated_fields={'slug':('name',)} 
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(category__shop__owner=request.user)
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser:
         if db_field.name =='category':
            kwargs['queryset'] = Category.objects.filter(shop__owner=request.user)   
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display=['shopName','owner','adress','registration_date','valid_from','valid_to','is_active']  
    def save_model(self, request, obj, form, change):
        if obj.valid_to < timezone.now():
            obj.is_active=False
        super().save_model(request, obj, form, change)
         

@admin.register(Product)
class PrductAdmin(admin.ModelAdmin):
    #override the formfield_for_foreignkey method of ModelAdmin 
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser:
            if db_field.name == 'shop':
                kwargs['queryset'] = Shop.objects.filter(owner=request.user)
            if db_field.name == 'category':
                kwargs['queryset'] = Category.objects.filter(shop__owner=request.user)  
            if db_field.name == 'subcategory':
               kwargs['queryset'] = SubCategory.objects.filter(category__shop__owner=request.user)   
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    list_display=[
        'name',
        'shop',
        'category',
        'price',
        'available',
        'created_date_time_format',
        'updated_date_time_format',
        'image_tag',
    ]
    list_filter=['available','created','updated']
    list_editable=['price', 'available']
    list_display_links=['image_tag','name']
    prepopulated_fields={'slug':('name',)}#this used to  automatically give value of name to  slug 
    list_per_page=5

    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(shop__owner=request.user)
    

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return 'No Image'
    image_tag.short_description = 'Product Image'

    def created_date_time_format(self,product):
        return product.created.date()
    created_date_time_format.short_description='created'

    def updated_date_time_format(self,product_obj):
        return product_obj.updated.date()
    updated_date_time_format.short_description='updated'

    






# Register your models here.
