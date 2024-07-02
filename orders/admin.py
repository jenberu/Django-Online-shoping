from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Order ,OrderItem
import csv
import datetime
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from django.utils.html import mark_safe
from django.template.defaultfilters import truncatechars

class OrderItemInline(admin.TabularInline):#An inline allows you to include a model on the same edit page as its related model.
     model=OrderItem
     raw_id_fields=['product']
def export_to_csv(modeladmin,request,queryset):
     opts=modeladmin.model._meta
     content_disposition={f'attachment; filename={opts.verbose_name}.csv'}
     response=HttpResponse(content_type='text/csv')
     response['Content-Disposition']=content_disposition
     writer=csv.writer(response)
     fields=[field for field in opts.get_fields()
             if not field.many_to_many and not field.one_to_many]
      # Write a first row with header information
     writer.writerow([field.verbose_name for field in fields])
     # Write data rows
     for obj in queryset:
          data_row=[]
          for field in fields:
               value=getattr(obj,field.name)
               if isinstance(value,datetime.datetime):
                    value=value.strftime('%d/%m/%Y')
               data_row.append(value)  
          writer.writerow(data_row)   
          return response  
     export_to_csv.short_description = 'Export to CSV File'
#add a link to each Order object on the list display page of the administration site
def order_detail(obj):#obj refers to the model instance
     url = reverse('orders:admin_order_detail', args=[obj.id])
     return mark_safe(f'<a class="btn btn-sm btn-outline-success" title="view order detial" href="{url}"><i class="fas fa-eye"></i></a>')
     """Django escapes HTML output by default. 
       You have to use the mark_safe function 
       to avoid auto-escaping."""
def order_to_pdf(obj):
      url = reverse('orders:admin_order_pdf', args=[obj.id])
      return mark_safe(f'<a class="btn btn-sm btn-outline-success" title="create PDF file" href="{url}"><i class="fas fa-file-pdf"></i></a>')
order_to_pdf.short_description='create PDF'

def update_status(obj):
     url=reverse('orders:updateStatus',args=[obj.id])
     return mark_safe(f'<a  class="btn btn-sm btn-outline-success" title="Edit status" href="{url}"> <i class="fas fa-pen "></i></a>')
update_status.short_description='update status'


def order_payment(obj):
     url=obj.get_stripe_url()
     truncated_stripe_id=truncatechars(obj.stripe_id,8)
     if obj.stripe_id:
          html=f'<a href="{url}" target="_blank">{truncated_stripe_id}</a>'
          return mark_safe(html)
     return ''
order_payment.short_description='Stripe Payment'





@admin.register(Order)
class  OrderAdmin(admin.ModelAdmin):
    actions=[export_to_csv]
    
    list_display = [
'id',
'shop',
 'first_name',
 'last_name',
 'email',
 'address',
 'postal_code',
 'city',
 'paid',
 order_payment,
 'created',
 'updated',
 'status',

  order_detail,#this add the above link to display on admin interface 
  order_to_pdf,
  update_status,
 ]  
    list_filter=['paid','created','updated']
    inlines=[OrderItemInline]
    list_per_page=5
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(shop__owner=request.user)
   

# Register your models here.
