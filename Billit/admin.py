from django.contrib import admin
from .models import inventory,bulk_import
class inv_admin(admin.ModelAdmin):
    search_fields=('product_id','category')
    list_display=('product_id','category','purchase_price','sales_status','sold_by')
    list_filter=('category','sold_by')
    
#admin.site.register(inventory)
admin.site.register(inventory,inv_admin)

admin.site.site_header = 'Paarijaatham Admin'


# Register your models here.
