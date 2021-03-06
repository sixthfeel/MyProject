from django.db import models

# Create your models here.


class AgencyInfo(models.Model):
	agencyno = models.CharField(max_length=9, verbose_name='销售商代码')
	agencyname = models.CharField(max_length=36, verbose_name='销售商')
	atype = (('券商', '券商'), ('银行', '银行'), ('保险', '保险'), ('第三方', '第三方'))
	agencytype = models.CharField(max_length=4, choices=atype, verbose_name='销售商类型')
	# models的choices属性作为新建数据时的下拉选项.
	onprd = (('已代销', '已代销'), ('未代销', '未代销'))
	agencyonprd = models.CharField(max_length=4, choices=onprd, verbose_name='是否代销')

	def __str__(self):
		return self.agencyno

	# models显示为中文名称.
	class Meta:
		verbose_name = '销售商信息'
		verbose_name_plural = '销售商信息'


class TestInfo(models.Model):
	testappl = models.CharField(max_length=12, verbose_name='申请人')
	testappldate = models.DateField(verbose_name='申请日')
	testcont = models.CharField(max_length=12, verbose_name='测试对接人')
	testcontno = models.CharField(max_length=15, verbose_name='联系方式')
	testcontmail = models.CharField(max_length=50, verbose_name='邮箱')
	testtype = models.CharField(max_length=10, verbose_name='测试类型', blank=True)
	teststartdate = models.DateField(verbose_name='测试开始日')
	testenddate = models.DateField(verbose_name='测试结束日', blank=True, null=True)
	tstatus = (('0', '未开始'), ('1', '测试完成'), ('2', '测试中'))
	teststatus = models.CharField(max_length=2, verbose_name='测试状态',  choices=tstatus,)
	agencyno = models.ForeignKey("AgencyInfo", verbose_name='销售商', on_delete=models.CASCADE)

	# models显示为中文名称.
	class Meta:
		verbose_name = '测试信息'
		verbose_name_plural = '测试信息'
