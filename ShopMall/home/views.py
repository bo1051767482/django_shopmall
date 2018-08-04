from django.shortcuts import render
from .models import shopping_car
from django.shortcuts import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.db.models import Q,F,Sum

# 购物车添加商品
def addcar(request):
    a = request.COOKIES.get('uid', 1)
    # return HttpResponse('进入')
    # print('进入')
    # print(request.POST)
    if a!=1:
        try:
            gid=request.POST['gid']
            num=request.POST['num']
            # print(num)
        except:
            return HttpResponse('商品不存在')
        c=shopping_car.objects.filter(goods_id=gid).values_list('goods_id',flat=True)

        gid=int(gid)
        if gid   in c:
            list="alert('成功添加到购物车')"
            shopping_car.objects.filter(goods=gid).update(number=F('number') + num)
            return HttpResponseRedirect(reverse('show',args=(gid,)))
            # return render(request,'goods/show_details.html')

        else:

            shopcar = shopping_car()
            shopcar.user_id = a
            shopcar.goods_id = gid
            shopcar.number = num
            shopcar.save()
            return HttpResponseRedirect(reverse('show',args=(gid,)))
    else:
        return HttpResponseRedirect(reverse('signin'))

# 删除购物车商品
def delcar(request):
    a=request.GET.get('p')
    shopping_car.objects.filter(id=a).delete()
    return HttpResponse(a)

#请求 购物车展示1
def showcar(request):
    return render(request, 'home/shopping_car.html')

#请求 个人中心
def my_center(request):
    return render(request, 'home/my_center.html')
    pass

#请求 我的订单
def order(request):
    return render(request,'home/user_page1.html')

#请求 我的收藏
def my_collect(request):
    return render(request, 'home/user_page2.html')
    pass

#请求 收货地址
def shop_address(request):
    return render(request, 'home/user_page3.html')
    pass

#请求 修改密码
def change_pwd(request):
    return render(request, 'home/user_page4.html')
    pass