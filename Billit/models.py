from django.db import models

class inventory(models.Model):
    product_id=models.CharField(primary_key=True,max_length=50)
    category=models.CharField(null=True,blank=True,max_length=300)
    purchase_price=models.IntegerField(null=True,blank=False)
    sold_price=models.IntegerField(null=True,blank=True)
    custodian=models.CharField(null=True,blank=True,max_length=100)
    induction_date=models.DateField(auto_now_add=True)
    sales_date=models.DateField(null=True,blank=True)
    purchase_date=models.DateField(auto_now_add=False,auto_now=False,null=True,blank=True)
    cust_name=models.CharField(null=True,blank=True,max_length=100)
    cust_phone=models.CharField(null=True,blank=True,max_length=100)
    cust_Email=models.EmailField(null=True,blank=True,max_length=100)
    profit=models.IntegerField(null=True,blank=True)
    sold_by=models.CharField(null=True,blank=True,max_length=100)
    prod_img=models.ImageField(null=True,blank=True)
    sales_status=models.CharField(null=True,blank=True,max_length=25,default="In Stock")
    
    def get_absolute_url(self):
        return "/home"
    
        
    


class bulk_import(models.Model):
    file_name=models.FileField(upload_to='data')
    
    
        
    