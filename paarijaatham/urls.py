"""paarijaatham URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_view
from paarijaatham import settings
from django.views import static
from API.views import getdetail
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', auth_view.login,{'template_name':'templates/login.html'},name='login_page'),
    url(r'^media/(.*)', static.serve,{'document_root':settings.MEDIA_ROOT}),
    url(r'^', include('Billit.urls')),
    url(r'^report_builder/', include('report_builder.urls')),
    url(r'^api/uat-interface/(?P<id>.*)', getdetail ,name='api_get_details'),
    

]
