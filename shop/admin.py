from typing import Any
from django.contrib import admin,messages
from django.db.models.query import QuerySet
from django.http import HttpRequest
from .models import Category,Product,SubCategory,Shop,ShopSubscrioptionPlan,ProductRecommandation,SocialMedia
from django.utils.html import mark_safe,format_html ,urlencode
from .forms import ProductAdminForm,SocialMediaForm
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ngettext


admin.site.register(ShopSubscrioptionPlan)
@admin.register(ProductRecommandation)
class ProductRecommendatonAdmin(admin.ModelAdmin):
    list_display=['product_id','purchased_with_product_id','purchased_with_times']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug','product_count']
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

@admin.register(SocialMedia)
class SocialMedaiAdmin(admin.ModelAdmin):
    form = SocialMediaForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser:
            if db_field.name == 'shop':
                kwargs['queryset'] = Shop.objects.filter(owner=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
class SocialMediaInline(admin.TabularInline):
    model=SocialMedia
    extra=1
    def get_queryset(self, request):
        qs=super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(shop__owner=request.user)
    def has_change_permission(self, request, obj= None):
        if request.user.is_superuser:
            return True
        if obj:#obj referse to the related object which is shop
           return request.user == obj.owner
        return super().has_change_permission(request, obj)
    def has_add_permission(self, request,obj=None):
       if request.user.is_superuser:
            return True
       if obj and obj.owner == request.user:
            return True
       return False
@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    inlines=[SocialMediaInline]
    actions=['deactivate_shop']
    list_display=['shopName','owner','adress','registration_date','valid_from','valid_to','is_active']  

    def get_actions(self,request):
        actions=super().get_actions(request)
        if not request.user.is_superuser:
            if 'deactivate_shop' in actions:
                del actions['deactivate_shop']
        return actions        
        # Override the save_model method to retain specific fields
    def save_model(self, request, obj, form, change):
        if obj.valid_to < timezone.now():
            obj.is_active=False

        if change:
            original_obj=Shop.objects.get(pk=obj.pk)
             # Retain the original values for specific fields
            obj.registration_date = original_obj.registration_date
            obj.valid_from = original_obj.valid_from
            obj.valid_to = original_obj.valid_to
            obj.is_active = original_obj.is_active     
        super().save_model(request, obj, form, change)
    def get_queryset(self, request):
         qs= super().get_queryset(request) 
         if request.user.is_superuser:
             return qs
         return qs.filter(owner=request.user)

         
   
        
    @admin.action(description="Refresh Selected Shops to Deactivate, if the subscription is expired ") 
    def deactivate_shop(self,request,queryset):
        for shop in queryset:
           if shop.valid_to < timezone.now():
               shop.is_active=False  
               shop.save()  
        self.message_user(
            request,
            #ngettext for singular and pluralization
            ngettext(
            "%d Shop was successfully Refreshed and expired shop is Deactivated ",
            "%d Shops were successfully Refreshed and expired shops are Deactivated ",
            len(queryset),

            )
            %len(queryset),
            messages.SUCCESS,
        )       
         
      
@admin.register(Product)
class PrductAdmin(admin.ModelAdmin):
    actions=['disable_avaliablity','enable_avaliablity']
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
        'slug',
        'available',
        'created_date_time_format',
        'updated_date_time_format',
        'image_tag',
    ]
    list_filter=['available','created','updated']
    list_editable=['price', 'available']
    list_display_links=['image_tag','name']
    list_per_page=5
    search_fields=['name']

    
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
    @admin.action(description='Disable avaliabilty for selected product')
    def disable_avaliablity(self,request,queryset):
        updated=queryset.update(available=False)
        self.message_user(
            request,
            ngettext(
            "%d Product was successfully Disabled it Avaliablity",
            "%d Products were successfully  Disabled thier Avaliablity",
            updated,
        )
        %updated,
        messages.SUCCESS,
        )
    @admin.action(description='Enable avaliablity for selected products')    
    def enable_avaliablity(self,request,queryset):
        updated=queryset.update(available=True)
        self.message_user(
            request,
            ngettext(
            "%d Product was successfully Enable its Avaliablity",
            "%d Products were successfully  Enable thier Avaliablity",
            updated,
        )
        %updated,
        messages.SUCCESS,
        )    
    






# Register your models here.
