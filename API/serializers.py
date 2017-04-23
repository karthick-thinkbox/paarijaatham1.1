from rest_framework import serializers
from Billit.models import inventory

class appserializer(serializers.ModelSerializer):
    class Meta:
        model=inventory
        fields=('product_id','sold_price','sales_date','sales_status',)
        