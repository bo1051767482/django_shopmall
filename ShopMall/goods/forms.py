from django import forms
from .widgets import TreeWidget
from .models import goods_type



class Myform(forms.ModelForm):
    parent_id=forms.IntegerField(widget=TreeWidget,required=False)


    class Meta:
        model=goods_type
        fields=['parent_id','name']#显示字段