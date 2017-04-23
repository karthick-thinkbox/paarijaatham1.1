from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from .forms import prod_search,salesform,importform
from django.template import Template,context
from django.http import HttpResponse
from .models import inventory
from django.views.generic.detail import DetailView
import csv ,os 
from datetime import date

@login_required(login_url='login_page')
def dashboard(request):
    
    current_user=request.user
    if request.method=="POST":
        sbox=prod_search(request.POST)
        if sbox.is_valid():
            item_id=sbox.cleaned_data['id']
            try:
                fetch_row=inventory.objects.get(pk = item_id)
                status=fetch_row.sales_status
                
                if status == "Sold Out":
                    
                    return redirect('sold_page',pk=item_id,flag="soldout")
                else:
                    return redirect('bill_page',uid=item_id)
                   
            except Exception as e:
                sbox=prod_search()
                dict={"user":current_user ,'form':sbox ,'Error':str(e)}
                return render(request,'base.html',dict)
    else:
        sbox=prod_search()
        dict={"user":current_user ,'form':sbox}
        return render(request,'base.html',dict)
 

@login_required(login_url='login_page') 
def exitpage(request):
    logout(request)
    return render (request,'logout.html')


def Autherror(request):
    sbox=prod_search()
    return render (request,'error.html',{'Error':'Auth' , 'form':sbox})

class soldpage(LoginRequiredMixin,DetailView):
    model=inventory
    template_name="templates/detail.html"
    login_url='login_page'
    '''def statflg(self):
        return self.flag
    '''
    
    def get_context_data(self ,**kwargs):
        context=super(soldpage,self).get_context_data(**kwargs)
        context['flg']=self.kwargs['flag']
        return context
    
  



@login_required(login_url='login_page') 
def billpage(request,uid):
    row=inventory.objects.get(pk=uid)
    status=row.sales_status
    soldby=row.sold_by
    current_user=request.user
    cat=row.category
    cost=row.purchase_price
    img=row.prod_img
    img=str(img)
    if request.method == "POST":
        if status =="Sold Out":
            return redirect('sold_page',pk=uid ,flag="soldout" )
        else:  
            form=salesform(request.POST,request.FILES ,instance=row)
            if form.is_valid():
                try:
                    
                    sales_price=form.cleaned_data['sold_price']
                    cname=form.cleaned_data['cust_name']
                    cemail=form.cleaned_data['cust_Email']
                    cmobile=form.cleaned_data['cust_phone']
                    sprofit=int(sales_price) - cost
                    #row=form.save(commit=False)
                    row.sold_price=sales_price
                    row.cust_name=cname
                    row.cust_phone=cmobile
                    row.cust_Email=cemail
                    row.profit=sprofit
                    row.sales_status="Sold Out"
                    row.sold_by=str(current_user)
                    row.sales_date=date.today()
                    row.save()
                    return redirect('sold_page',pk=uid,flag="deal")
                except Exception as e:
                    #form=salesform(initial={'product_id':uid,'category':cat})
                    return render(request,'bill_page.html',{"form":form ,'img':img ,'cat':cat,'Error':str(e)})
                    
                        
                        
            
            
        
            else:
                form=salesform(initial={'product_id':uid,'category':cat})
                return render(request,'bill_page.html',{"form":form ,'img':img ,'cat':cat,'flg':'Validation_Error'})    
                    
    else:
        form=salesform(initial={'product_id':uid,'category':cat})
        return render(request,'bill_page.html',{"form":form ,'img':img ,'cat':cat})

@login_required(login_url='login_page') 
@permission_required('Billit.add_bulk_import' ,login_url='Error_page')
def bulkload(request):
    if request.method == "POST" :
        form=importform(request.POST ,request.FILES)
        if form.is_valid():
            fileobj=form.save()
            fileurl=fileobj.file_name.url
            basepath=r'C:/Users/acer/Desktop/Djangoworkouts/paarijaatham/Billit/'
            #BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            #normpath=os.path.normpath(fileurl)
            final_path=basepath+fileurl
            
            
            try:
                
                with open(final_path,'r') as f:
                    reader=csv.reader(f)
                    row=next(reader)
                    if(row[0]=='Product_id' and row[1] =='category'and row[2]=='purchase_price' and row[3]=='custodian' and row[4]=='purchase_date' and row[5]=='img_path'):
                        for line in reader:
                            stat,record=inventory.objects.get_or_create(
                                                                    product_id=line[0],
                                                                    category=line[1],
                                                                    purchase_price=line[2],
                                                                    custodian=line[3],
                                                                    purchase_date=line[4],
                                                                    prod_img=line[5]
                                                                    )
                        
                        form=importform()
                        return render(request,'upload_page.html',{"form":form ,"stat":'Success'})
                    else:
                        form=importform()
                        return render(request,'upload_page.html',{'Header_error':"Header" ,"form":form})
            
            except Exception as e:
                form=importform()
                return render(request,'upload_page.html',{'Error':str(e) ,'form':form})
                                                                    
    else:
        
        form=importform()
        return render(request,'upload_page.html',{"form":form})
        
            