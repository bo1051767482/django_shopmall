from django.conf.urls import url
from django.contrib import admin
import xadmin
from . import views

urlpatterns = [
    url(r'^addcar/',views.addcar,name='addcar'),
    url(r'^showcar/',views.showcar,name='showcar'),
    url(r'^delcar/',views.delcar,name='delcar'),
    url(r'^order/',views.order,name='order'),
    url(r'^my_center/',views.my_center,name='my_center'),
    url(r'^my_collect/',views.my_collect,name='my_collect'),
    url(r'^shop_address/',views.shop_address,name='shop_address'),
    url(r'^change_pwd/',views.change_pwd,name='change_pwd'),
]