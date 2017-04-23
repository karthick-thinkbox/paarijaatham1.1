from django.conf.urls import url
from .views import dashboard,exitpage,billpage,bulkload,Autherror
from . import views  

urlpatterns = [
    
    url(r'^home/$', dashboard,name='home_page'),
    url(r'^exit/', exitpage,name='exit_page'),
    url(r'^detail/(?P<pk>[\w\d]+)/(?P<flag>[\w]+)', views.soldpage.as_view(),name='sold_page'),
    url(r'^billit/(?P<uid>[\w\d]+)/', billpage,name='bill_page'),
    url(r'^upload/', bulkload,name='upload_page'),
    url(r'^Autherror/$', Autherror,name='Error_page')
    
    #url(r'search/(?P<prod_code>[\w\d]+)', Billpage,name='Bill_page'),
]
