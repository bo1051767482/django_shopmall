from home.models import shopping_car

def public_car(request):
    a = request.COOKIES.get('uid', 1)
    data=[]
    total=0
    number=0
    if a !=1:
        data=shopping_car.objects.filter(user=a)

        # print(data.__dict__)
        for x in data:
            total+=x.goods.price+(x.goods.price*x.number)
            # x.goods.price*x.number
            #单个商品数量
            # print(x.number)
            #图片路径打印
            # p1=x.goods.goods_img_set.first()
            # print(p1.path)
            number+=1
    return {'data':data,'total':total,'number':number}