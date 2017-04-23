from django import forms
from django.forms import ModelForm
from .models import inventory,bulk_import

class prod_search(forms.Form):
    
    id=forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Product_id"}),label="UID")
    
    
class salesform(ModelForm):
    sold_price=forms.IntegerField(required=True)
    class Meta:
        model=inventory
        fields=['product_id','category','sold_price','cust_name','cust_phone','cust_Email']
        widgets={
                 'product_id':forms.TextInput(attrs={"Readonly":True}),
                 'category':forms.TextInput(attrs={"Readonly":True}),
                 
                 }
        labels={
                 
                 'cust_name':"Customer Name",
                 'cust_phone':"Mobile",
                 'cust_Email':"Email",
                 'sold_price': "Sales Price",
                 
                }
    def __init__(self,*args,**kwargs):
        super(salesform,self).__init__(*args,**kwargs)
        self.fields['sold_price'].required=True
        self.fields['cust_name'].required=True
        self.fields['cust_phone'].required=True
        self.fields['cust_Email'].required=True




class importform(ModelForm):
    class Meta:
        model=bulk_import
        fields=['file_name']
        labels={
                 'file_name':''
                }