from django.contrib import admin
from .models import New,Advertisment,AddsImage
admin.site.register(New)
@admin.register(AddsImage)
class AddsImageAdmin(admin.ModelAdmin):
    list_display = ('id','adds', 'image')
    #delete global action
    def get_actions(self,request):
       actions=super().get_actions(request)
       if 'export_to_csv' in actions:
          del actions['export_to_csv']
       return actions   
@admin.register(Advertisment)
class AdvertismentAdmin(admin.ModelAdmin):
  list_display = ('title', 'start_date', 'end_date', 'active')
  list_filter = ('active',)
  search_fields = ('title',)



