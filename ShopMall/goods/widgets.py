# coding: utf-8
from django import forms
from .models import goods_type
import json

html = """
	<link rel="stylesheet" href="/static/ztree/demo.css" type="text/css">
	<link rel="stylesheet" href="/static/ztree/zTreeStyle.css" type="text/css">
	<script type="text/javascript" src="/static/ztree/jquery.ztree.core.js"></script>
	<SCRIPT type="text/javascript">
		<!--
		var setting = {
			data: {
				simpleData: {
					enable: true
				}
			},
			callback: {
				onClick: onClick
			}
		};

		var zNodes =%s;

		$(document).ready(function(){
			$.fn.zTree.init($("#treeDemo"), setting, zNodes);
		});
		
		
		function onClick(e, treeId, treeNode) {
			var zTree = $.fn.zTree.getZTreeObj("treeDemo"),
			nodes = zTree.getSelectedNodes(),
			v = "";
			nodes.sort(function compare(a,b){return a.id-b.id;});
			for (var i=0, l=nodes.length; i<l; i++) {
				v = nodes[i].id;
			}
			console.log(v)
			$('#%s').val(v);
		}

		
		
		
		//-->
	</SCRIPT>
"""


class TreeWidget(forms.Textarea):

    def __init__(self, mode="", theme="", attrs=None):
        super(TreeWidget, self).__init__(attrs)
        self.mode = mode
        self.theme = theme

    def render(self, name, value, attrs=None):
        lis = goods_type.objects.filter().extra({'pId': 'parent_id'}).values('id','name','pId',)
        json_data=json.dumps(list(lis))

        return html % (json_data,name) + """<div class="zTreeDemoBackground left">
		            <ul id="treeDemo" class="ztree"></ul>
		            <input type='hidden' name='%s' id='%s' value='0' />
	            </div>""" % (name, name)
