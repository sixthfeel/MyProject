import xlwt
from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.http import StreamingHttpResponse


# Register your models here.

# site_title设置为系统名称，会在浏览器标签上显示
admin.site.site_title = "华泰资管代销接入管理"
# site_header设置为系统名称，会在首页显示
admin.site.site_header = "华泰资管代销接入管理"
# index_title设置为admin页面的标签
admin.site.index_title = "代销测试信息维护"


class AgencyInfoAdmin(admin.ModelAdmin):
	actions = ["saveexecl"]
	list_display = [
		'agencyno', 'agencyname', 'agencytype', 'colored_agencyonprd'
	]
	list_display_links = ['agencyno']
	list_filter = ['agencyno', 'agencyonprd']
	search_fields = ['agencyno']
	list_per_page = 20

	def colored_agencyonprd(self, obj):
		if obj.agencyonprd == '已代销':
			color_code = 'green'
		else:
			color_code = 'red'
		return format_html('<span style="color: {};">{}</span>', color_code, obj.agencyonprd,)
	colored_agencyonprd.short_description = u"是否代销"

	def get_readonly_fields(self, request, obj=None):
		# 重新定义此函数，限制普通用户所能修改的字段
		if request.user.is_superuser:
			self.readonly_fields = []
		return self.readonly_fields

	readonly_fields = ['colored_agencyonprd']

	def saveexecl(self, request, queryset):
		Begin = xlwt.Workbook()
		sheet = Begin.add_sheet("response")
		cols = 0
		for query in queryset:
			# you need write colms                     # 好像有个方法可以一次性写入所有列，记不清了，只能用这种简单的方法去实现
			sheet.write(cols, 1, str(query.agencyno))  # 写入第一列
			sheet.write(cols, 2, str(query.agencyname))  # 写入第二列
			sheet.write(cols, 3, str(query.agencytype))  # 写入第三列
			cols += 1
		Begin.save("%s" % ('filename'))

		def file_iterator(filename, chuck_size=512):
			with open(filename, "rb") as f:
				while True:
					c = f.read(chuck_size)
					if c:
						yield c
					else:
						break

		response = StreamingHttpResponse(file_iterator('filename'))
		response['Content-Type'] = 'application/octet-stream'
		response['Content-Disposition'] = 'attachment;filename="{}"'.format("result.xls")
		return response

	saveexecl.short_description = "导出Excel"  # 按钮显示名字


class TestInfoAdmin(admin.ModelAdmin):
	# list_display设置要显示在列表中的字段
	list_display = [
		'testserno', 'colored_teststatus', 'agencyno', 'get_agencyname', 'testappl', 'testappldate', 'testcont', 'testcontno',
		'testcontmail', 'teststartdate', 'testenddate'
	]
	# list_filter筛选器
	list_filter = ['agencyno', 'teststartdate', 'testenddate']
	# search_fields搜素栏,外键要用agencyno__agencyname的形式查询
	search_fields = ['agencyno__agencyname', 'testappl', 'colored_teststatus']
	# ordering设置默认排序字段，负号表示降序排序
	ordering = ('-testappldate',)
	# list_per_page分页条数
	list_per_page = 20

	# 根据测试开始时间，销售商代码，主键id生成测试序号
	def testserno(self, obj):
		testno1 = obj.teststartdate.strftime("%Y%m%d")
		testno2 = obj.agencyno
		testno3 = obj.id
		testserno = str(testno1) + '-' + str(testno2) + '-' + str(testno3)
		return testserno
	testserno.short_description = u"测试序号"

	def get_agencyname(self, obj):
		return obj.agencyno.agencyname
	get_agencyname.short_description = u"销售商名称"

	def colored_teststatus(self, obj):
		if obj.teststatus == '1':
			color_code = 'green'
		else:
			color_code = 'red'
		return format_html('<span style="color: {};">{}</span>', color_code, obj.get_teststatus_display(),)
	colored_teststatus.short_description = u"测试状态"


admin.site.register(AgencyInfo, AgencyInfoAdmin)
admin.site.register(TestInfo, TestInfoAdmin)
