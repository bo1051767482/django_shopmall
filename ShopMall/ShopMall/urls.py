"""ShopMall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
import xadmin
from django.conf import settings  #获取配置文件
from django.conf.urls.static import static  #获取静态文件

urlpatterns = [
    url(r'^admin/', xadmin.site.urls),

    url(r'', include('goods.urls')),
    url(r'^home/', include('home.urls')),


    url(r'^ueditor/',include('DjangoUeditor.urls'))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  #图片显示设置