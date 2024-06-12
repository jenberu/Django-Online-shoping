from django.contrib import admin
from .models import Category,Product
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}



@admin.register(Product)
class PrductAdmin(admin.ModelAdmin):
    list_display=[
        'name',
        'slug',
        'price',
        'available',
        'created',
        'updated',
        'image'
    ]
    list_filter=['available','created','updated']
    list_editable=['price', 'available']
    prepopulated_fields={'slug':('name',)}#this used to  automatically give value of name to  slug 






# Register your models here.
