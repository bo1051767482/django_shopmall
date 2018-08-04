from django.http.response import HttpResponse #返回内容方法
from django.http.response import HttpResponseRedirect  #返回页面重定向
from django.shortcuts import render,render_to_response  #返回渲染页面
from .models import * #导入全部商品表
from django.core.paginator import Paginator  #导入分页模块方法
# Create your views here.
from home.models import *  #导入home 全部表
from django.db.models import Sum, Q, F  #返导入django的数学方法
from PIL import  ImageDraw,Image,ImageFont #导入验证码工具画笔 画布
from io import  BytesIO  #导入io存入对象到内存
import random  #随机数
import json   #返回给ajax以json数据方式
from django.core.urlresolvers import reverse  #url的反向解析

#主页
def zhuye(request):

    li="<a href='list/'>跳转list</a>"
    return render(request,'goods/index.html')


#商品列表
def list(request):

    li=goods.objects.filter().order_by('id')          #取出全部数据
    # for i in li:
    #     img=i.goods_img_set.first()
    #     if img:
    #         print(img.path)

    # print(li)
    p=Paginator(li,5)             #定义每页显示数量
    page=request.GET.get('p',1)   #获取get用户请求页码默认返回1
    data=p.page(page)                 #返回用户请求页码数据

    # recommend_list = goods_tj.objects.all().order_by('goodstj_sort_id')
    # for recom in recommend_list:
    #     print('对象:',recom.goodstj_name.name)
    #     print('图像:',recom.goodstj_name.goods_img_set.first().path)

    # print(data.paginator.__dict__)  #格式化字典显示

    return render(request,'goods/list.html',{'li':data})


# 商品详情页面
def show(request,id):
    # print(id)
    li = goods_img.objects.filter(goods=id).values('path')
    info=goods.objects.get(id=id)
    print('adsfds',info.goods_evaluate_set.all())
    #评价数量
    ev_num=len(info.goods_evaluate_set.all())
    # print(len(a))
    return render(request, 'goods/show_details.html', {'li':li, 'info':info,'ev_num':ev_num})


# showdetil下面页码操作
def page(request,id):

    upage=request.GET.get('p',1)
    evaluate=request.GET.get('t',0)
    if int(evaluate)!=0:
        info = goods_evaluate.objects.filter(goods_id=id,evaluate_type=evaluate).order_by('id')
        # print('类型:',info)
    else:
        info = goods_evaluate.objects.filter(goods_id=id).order_by('id')
    # print(upage)

    p=Paginator(info,1)
    data=p.page(upage)
    # print('data:',data)
    a=goods_tj.objects.all().order_by('goodstj_sort_id')
    # print(a[0].goodstj_name)  #获取商品名字id
    # for recom in a:
    #     print(recom)

    return  render(request,'goods/evaluate_ajax.html',{'data':data,'type':evaluate})


#商品推荐
def goodstj(request):

    recommend_list = goods_tj.objects.all().order_by('goodstj_sort_id')
    # if uid==1:
    #     return  render(request,'goods/public_goos_recm.html',{'recommend':recommend_list})
    # else:
    return render(request, 'public/public_goos_recm.html', {'recommend': recommend_list})

#请求主页
def index(request):
    return render(request,'goods/index.html')

#请求登陆界面
def signin(request):
    return render(request,'goods/signIn.html')


#请求注册界面
def signup(request):
    return render(request,'goods/signUp_1.html')


#注册登录方法
def reg(request):

    #注册方法
    if request.POST['submit']=='注册':
        admin_if=member.objects.all().values_list('name',flat=True)#将默认的列表套元祖转换为列表

        # print(admins.objects.all().values_list('username'))#列表套元祖
        # print(admin_if)

        qname=request.POST['p_name']
        # print(qname)
        pwd=request.POST['pwd']
        if qname not in admin_if:
            #判断验证码
            if request.session['forget_pwd'].lower() == request.POST['auth']:
                member.objects.create(password=pwd,name=qname)
                # return HttpResponse('注册成功')
                return  msg('注册成功,跳转至首页',reverse(index))
                # print('msgasfddddddddda111111111111111111111')
                # return  render(request,'goods/signUp_2.html',{'submit':request.POST['submit']})

            #验证码不对方法
            else:
                lis="alert('验证码错误')"
                return render(request, 'goods/signUp_1.html',{'list':lis})
        else:
            lis = "alert('用户名已存在')"
            return render(request, 'goods/signUp_1.html', {'list': lis})
            # return  msg('用户名已存在', reverse(signup))
    #登陆方法
    else:
        r1=member.objects.filter((Q(name=request.POST['p_name'])&Q(password=request.POST['pwd'])))
        # print(r1)
        try:
            a=r1[0].name
            b=r1[0].password
            # print(type(a))
            # print(b)
            #判断图形验证码
            if request.session['forget_pwd'].lower()== request.POST['auth']:

                # re=render(request,'goods/signUp_2.html',{'submit':request.POST['submit']})
                re=msg('注册成功,跳转至首页',reverse(index))
                name_id=member.objects.filter(name=a).values('id')

                re.set_cookie('uid',name_id[0]['id'])

                return  re
            else:
                lis = "alert('验证码错误')"
                return render(request, 'goods/signIn.html', {'list': lis})
        except:
            lis = "alert('账号不存在')"
            return render(request, 'goods/signIn.html', {'list': lis})


#验证码 方法
def forget_pwd(request):
    width=69
    height=38
    #创建画布
    im=Image.new("RGB",(width,height),(random.randint(30,200),random.randint(30,200),200))
    #创建画笔
    draw=ImageDraw.Draw(im)
    #验证码备选值
    str='ABCDEF123GHIJKLMNO45670PQRSTUVWXYZ'
    #起始位置
    position=5
    code_str=''
    #引入字体参数有字体 ,大小
    font=ImageFont.truetype('mvboli.ttf',25)
    #画字体
    for x in range(0,4):
        code=str[random.randint(0,len(str)-1)]
        draw.text((position,1),code,font=font)
        position+=15
        code_str+=code
        #画噪点
    for y in range(0,150):
        xy=(random.randint(0,150),random.randint(0,25))
        fill=(random.randint(0,255),255,random.randint(0,255))
        draw.point(xy,fill=fill)
    draw.line((0,15,69,19),(0,0,0))
    buf=BytesIO()
    im.save(buf,'png')
    request.session['forget_pwd']=code_str
    return HttpResponse(buf.getvalue(),'images/png')


#cookie
def cookie(request):
    a = request.COOKIES.get('uid', 1)
    # print(a)
    if a!=1:
        username=member.objects.filter(id=a).values_list('name',flat=True)
        # print(username[0])
        content=json.dumps(username[0])
        return  HttpResponse(content)
    else:
        b='请登陆'
        content=json.dumps(b)
        return HttpResponse(content)


#退出账户方法
def logout(request):

    re = HttpResponseRedirect(reverse(list))
      # 清理cookie里保存uid

    re.delete_cookie('uid')

    return re

#ajax判断账户名
def ajax_forget_user(request):
    user_name=request.GET.get('p',1)
    b=member.objects.filter(name=user_name).values_list('name',flat=True)
    if user_name not in b:
        return HttpResponse(1)
    else:
        return HttpResponse(0)


def search(request):
    a=request.GET.get('input')
    print(a)
    # return render(request,'goods/list.html')
    return HttpResponseRedirect(reverse(list))

def msg(msg, url, second=3):

    return render_to_response('goods/signUp_2.html', {'msg': msg, 'url': url, 'second': second})