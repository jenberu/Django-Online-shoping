from django.contrib import admin

from .models import UserProfile
from django.utils.html import mark_safe

class UserProfileAdmin(admin.ModelAdmin):
    list_display=['user','first_name','last_name','image_tag']
    list_filter=['first_name']
    list_per_page=5

    def image_tag(self,obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50"/>')
        return 'No image'
    image_tag.short_description = 'Profile Image'
admin.site.register(UserProfile,UserProfileAdmin)

