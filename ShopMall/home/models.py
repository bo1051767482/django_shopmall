from django.db import models

# Create your models here.


class member(models.Model):       #会员信息表

    sex_choice=((0,'不设置'),(1,'男'),(2,'女'))

    # id=models.AutoField(primary_key=True,)                    #主键自动增长一般不用创建
    nickname=models.CharField(max_length=30,default='admin',verbose_name='昵称')
    name=models.CharField(max_length=30,unique=True,verbose_name='用户名')
    password=models.CharField(max_length=32,verbose_name='用户密码')
    sex=models.IntegerField(default=0,choices=sex_choice,verbose_name='性别')  #choice给个下拉框
    email=models.CharField(max_length=40,default=0,verbose_name='邮箱')
    phone=models.CharField(max_length=11,default=0,null=False,verbose_name='手机')
    qq=models.CharField(max_length=20,default=0,null=False,verbose_name='QQ')

    create_time=models.DateTimeField(auto_now_add=True,verbose_name='账户创建时间')         #创建帐户时间
    last_login_time=models.DateTimeField(auto_now=True, verbose_name='最后一次登录时间')                      #每一次操作时间记录,参数是auto_now=默认不写就是


    def __str__(self):
        return self.name
    class Meta:
        verbose_name='用户'
        verbose_name_plural='用户信息'


class shopping_car(models.Model):
    user=models.ForeignKey('member',default=1,verbose_name='用户名')
    number=models.IntegerField(default=1,verbose_name='数量')
    goods=models.ForeignKey('goods.goods',default=1,verbose_name='商品ID')
    uptime=models.DateTimeField(auto_now=True,verbose_name='更新时间')

    def __str__(self):
        return self.user

    class Meta:
        verbose_name='购物车商品信息'
        verbose_name_plural='购物车表'