from django.db import models

# Create your models here.


class AgencyInfo(models.Model):
    agencyno = models.CharField(max_length=9, verbose_name='销售商代码')
    agencyname = models.CharField(max_length=36, verbose_name='销售商')
    agencytype = models.CharField(max_length=4, verbose_name='销售商类型')
    agencyonprd = models.CharField(max_length=2, verbose_name='已代销')

    def __str__(self):
        return self.agencyname


class TestInfo(models.Model):
    testno = models.CharField(max_length=14, verbose_name='测试编号')
    testappl = models.CharField(max_length=12, verbose_name='申请人')
    testappldate = models.DateField(verbose_name='申请日')
    testcont = models.CharField(max_length=12, verbose_name='测试对接人')
    testcontno = models.CharField(max_length=15, verbose_name='联系方式')
    testcontmail = models.CharField(max_length=50, verbose_name='邮箱')
    testtype = models.CharField(max_length=10, verbose_name='测试类型')
    teststartdate = models.DateField(verbose_name='测试开始日')
    testenddate = models.DateField(verbose_name='测试结束日')
    teststatus = models.CharField(max_length=2, verbose_name='测试状态')
    agencyno = models.ForeignKey("AgencyInfo", on_delete=models.CASCADE)

    def __str__(self):
        return self.testno
