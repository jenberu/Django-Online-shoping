from django.contrib import admin
from .models import Category,Product,SubCategory,Shop
from django.utils.html import mark_safe

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(shop__owner=request.user)
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display=['name','category','slug']
    prepopulated_fields={'slug':('name',)} 
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(category__shop__owner=request.user)
@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display=['shopName','owner','adress','registration_date']   



@admin.register(Product)
class PrductAdmin(admin.ModelAdmin):
    list_display=[
        'name',
        'slug',
        'price',
        'available',
        'created',
        'updated',
        'image_tag',
    ]
    list_filter=['available','created','updated']
    list_editable=['price', 'available']
    prepopulated_fields={'slug':('name',)}#this used to  automatically give value of name to  slug 
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
    






# Register your models here.
