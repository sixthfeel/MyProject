from django.contrib import admin
from .models import *

# Register your models here.

# site_title设置为系统名称，会在浏览器标签上显示
admin.site.site_title = "华泰资管代销接入管理"
# site_header设置为系统名称，会在首页显示
admin.site.site_header = "华泰资管代销接入管理"
# index_title设置为admin页面的标签
admin.site.index_title = "代销测试信息维护"


class AgencyInfoAdmin(admin.ModelAdmin):
	list_display = [
		'agencyno', 'agencyname', 'agencytype', 'colored_agencyonprd'
	]
	list_filter = ['agencyno', 'agencyonprd']
	search_fields = ['agencyno']
	list_per_page = 20


class TestInfoAdmin(admin.ModelAdmin):
	# list_display设置要显示在列表中的字段
	list_display = [
		'testno', 'agencyno', 'testappl', 'testappldate', 'testcont', 'testcontno',
		'testcontmail', 'teststartdate', 'testenddate', 'teststatus'
	]
	# list_filter筛选器
	list_filter = ['agencyno', 'teststartdate', 'testenddate']
	# ordering设置默认排序字段，负号表示降序排序
	ordering = ('-testappldate',)
	# list_per_page分页条数
	list_per_page = 20


admin.site.register(AgencyInfo, AgencyInfoAdmin)
admin.site.register(TestInfo, TestInfoAdmin)
