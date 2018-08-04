from django.db import models

# Create your models here.
from DjangoUeditor.models import UEditorField

#商品信息
class goods(models.Model):
    delete=((0,'否'),(1,'是'))
    name=models.CharField(max_length=150,verbose_name='商品名名称')
    title=models.CharField(max_length=150,verbose_name='商品说明')
    price=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='价格')
    promotion_price=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='促销价')
    type_id=models.ForeignKey('goods_type',default=1,verbose_name='分类ID')
    disabled=models.IntegerField(default=0,choices=delete)
    stoc=models.IntegerField(default=0,verbose_name='库存')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='商品'
        verbose_name_plural='商品信息'

#商品介绍
class goods_introduce(models.Model):
    content=UEditorField(u'产品特色',height=300,width=800,max_length=10240000000000000,default=u'',blank=True,imagePath='ueditor/',toolbars='full',filePath='files/')
    content2=UEditorField(u'产品功能',height=300,width=800,max_length=10240000000000000,default=u'',blank=True,imagePath='ueditor/',toolbars='full',filePath='files/')
    content3=UEditorField(u'产品细节',height=300,width=800,max_length=10240000000000000,default=u'',blank=True,imagePath='ueditor/',toolbars='full',filePath='files/')
    content4=UEditorField(u'产品信息',height=300,width=800,max_length=10240000000000000,default=u'',blank=True,imagePath='ueditor/',toolbars='full',filePath='files/')


    afte_sale=UEditorField(u'售后',height=300,width=800,max_length=10240000000000000,default=u'',blank=True,imagePath='ueditor/',toolbars='full',filePath='files/')
    goods=models.OneToOneField('goods',default=1,to_field='id')

    class Meta:
        verbose_name='商品介绍'
        verbose_name_plural='商品详细信息'

#商品图片
class goods_img(models.Model):
    path=models.ImageField(upload_to='goods',max_length=200,verbose_name='图片路径')
    goods=models.ForeignKey('goods',default=1,verbose_name='商品ID')  #一对多外键对应商品ID
    status=models.IntegerField(default=0,verbose_name='状态')
    # def __str__(self):
    #     return self.goods

   #给字段直接显示缩略图
    def img_tab(self):

        return  "<img src='/media/%s' width='50' height='50' />" %(self.path)

    img_tab.short_description='图片'
    img_tab.allow_tags = True

    # end给字段直接显示缩略图

    #该字段起别名
    class Meta:
        verbose_name='商品图片'
        verbose_name_plural='商品内容图片'

    #end该字段起别名

#商品评价
class goods_evaluate(models.Model):
    start=((1,1),(2,2),(3,3),(4,4),(5,5),)
    start_type=((1,'差评'),(2,'中评'),(3,'好评'),)
    uid=models.ForeignKey('home.member',default=1,verbose_name='用户ID')
    create_time=models.DateTimeField(auto_now_add=True,verbose_name='评价时间')
    goods_id=models.ForeignKey('goods',default=1,verbose_name='商品ID')

    evaluate_content=models.TextField(verbose_name='评价内容')
    evaluate_img=models.ImageField(blank=True,upload_to='goods',max_length=200,verbose_name='评价图片路径')

    evaluate_star=models.IntegerField(default=5,verbose_name='评价星级',choices=start)
    evaluate_type=models.IntegerField(default=5,verbose_name='好评度',choices=start_type)


    # 给字段直接显示缩略图
    def img_tab(self):

        return "<img src='/media/%s' width='50' height='50' />" % (self.evalute_img)

    img_tab.short_description = '图片'
    img_tab.allow_tags = True

    # end给字段直接显示缩略图

    class Meta:
        verbose_name='商品评价'
        verbose_name_plural='商品评价信息'

#商品推荐
class goods_tj(models.Model):
    goodstj_name=models.ForeignKey('goods',verbose_name='商品ID')
    goodstj_sort_id=models.IntegerField(default=1)
    goodstj_start_time=models.DateTimeField()
    goodstj_end_time=models.DateTimeField()

    class Meta:
        verbose_name='商品推荐'#字段名
        verbose_name_plural='商品推荐表'#表名
#商品分类
class goods_type(models.Model):
    #类别名
    name=models.CharField(max_length=100,verbose_name='类别名')
    parent_id=models.IntegerField(default=0,verbose_name='父类ID')


    class Meta:
        verbose_name='商品分类'#字段名
        verbose_name_plural='商品分类表表'#表名
    def __str__(self):
        return self.name




