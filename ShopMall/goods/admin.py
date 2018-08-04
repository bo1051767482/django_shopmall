from django.contrib import admin
import xadmin
# from DjangoUeditor.models import UEditorField
from .models import goods,goods_evaluate,goods_img,goods_introduce,goods_tj,goods_type
# Register your models here.

#引入钩子监测提交时触发钩子
from xadmin.views import  filter_hook
from .forms import Myform

class goodsAdmin():
    list_display=['name','price','disabled','stoc']
    #替换按钮  修改商品时保存为新的开一个另存为的按钮
    save_as = True
xadmin.site.register(goods,goodsAdmin)



class goodsevaluate():
    list_display=['uid','evaluate_type','img_tab','create_time','evaluate_star']  #定义显示图片缩率图
    # 只读字段
    readonly_fields = ['evaluate_type']
    show_detail_fields = ['evaluate_img']
    @filter_hook
    def save_models(self):
        num=self.new_obj.evaluate_star
        if num>=4:
            self.new_obj.evaluate_type=3
        elif num>=3:
            self.new_obj.evaluate_type = 2
        else:
            self.new_obj.evaluate_type = 1

        # print(self.new_obj.evaluate_star)


        #保存数据
        self.new_obj.save()

xadmin.site.register(goods_evaluate,goodsevaluate)

class goodsimg():
    list_display=['status','img_tab','goods']

    #给字段加状态代码edi table
    list_editable=['status','goods',]

    #在字段后加详细小按钮
    show_detail_fields=['goods']



xadmin.site.register(goods_img,goodsimg)


class  introduceAdmin():
    #注册ueditor的模板类型要在这注册
    style_fields={'content':'ueditor','content2':'ueditor','content3':'ueditor','content4':'ueditor','afte_sale':'ueditor'}

xadmin.site.register(goods_introduce,introduceAdmin)

class goodstj_Admin():
    list_display = ['goodstj_name', 'goodstj_sort_id', 'goodstj_start_time','goodstj_end_time']

xadmin.site.register(goods_tj,goodstj_Admin)


class goodstype_Admin():
    form=Myform
    #分类表批量添加
    @filter_hook
    def save_models(self):
        # print(self.request.resolver_match.url_name)  #地址栏地址等于goods_goods_type_add
        if self.request.resolver_match.url_name=='goods_goods_type_add':
            context=self.new_obj.name
            # print(context) #打印添加的类名
            type_lis=context.split(',') #分割后
            print(type(type_lis))
            for x in type_lis:
                if self.new_obj.id!=None:
                    self.new_obj.id=None
                self.new_obj.name=x
                self.new_obj.save()
            else:
                self.new_obj.save()
xadmin.site.register(goods_type,goodstype_Admin)