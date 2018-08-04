from django.conf.urls import url
from django.contrib import admin
from django.conf import settings  #获取配置文件
from django.conf.urls.static import static  #获取静态文件
import xadmin
from . import views


urlpatterns = [

    url(r'^$',views.zhuye ),
    url(r'^list/$',views.list ,name='list'),
    url(r'^show/(\d+)/',views.show,name='show'),
    url(r'^signin/', views.signin, name='signin'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^reg/',views.reg,name='reg'),
    url(r'^index/',views.index,name='index'),
    url(r'^search/',views.search,name='search'),

    #ajax请求

    url(r'^cookie/',views.cookie,name='cookie'),
    url(r'^logout/',views.logout,name='logout'),
    url(r'^forget_pwd/',views.forget_pwd,name='forget_pwd'),
    url(r'^recommend/',views.goodstj,name='goodstj'),
    url(r'^upage/(\d+)/',views.page,name='page'),
    url(r'^ajax_forget_user/',views.ajax_forget_user,name='ajax_forget_user'),


]
