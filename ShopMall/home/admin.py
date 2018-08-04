
import xadmin
from xadmin import views
from .models import member,shopping_car
# Register your models here.

#开启全局主题
class BaseSetting():
    enable_themes = True  # 开启主题
    use_bootswatch = True  # 使用样例
xadmin.site.register(views.BaseAdminView, BaseSetting)


#全局设置
class GlobalSetting(object):
    site_title='乐选商城后台管理'  #网页头部
    site_footer='乐选商城-------联系我们:120'  #网页底部
    default_model_icon = "{User: 'user-icon'}"  #网页图标
xadmin.site.register(views.CommAdminView, GlobalSetting)

#member表设置
class MemberAdmin():
    list_display = ['id','nickname','name','sex','last_login_time']
    site_title='乐选商城后台管理'
    site_footer='乐选商城-------联系我们:130'
    default_model_icon="{User: 'user-icon'}"

xadmin.site.register(member, MemberAdmin)

class shoppincarAdmin():
    list_display = ['id', 'goods', 'user']

xadmin.site.register(shopping_car,shoppincarAdmin)