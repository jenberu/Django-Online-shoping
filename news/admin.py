from django.contrib import admin
from .models import New,Advertisment
admin.site.register(New)

@admin.register(Advertisment)
class AdvertismentAdmin(admin.ModelAdmin):
  list_display = ('title', 'start_date', 'end_date', 'active')
  list_filter = ('active',)
  search_fields = ('title',)


