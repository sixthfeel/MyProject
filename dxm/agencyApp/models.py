from django.db import models

# Create your models here.


class AgencyInfo(models.Model):
    agencyno = models.CharField(max_length=9)
    agencyname = models.CharField(max_length=36)
    agencytype = models.CharField(max_length=4)

    def __str__(self):
        return self.agencyname

class TestInfo(models.Model):
    testno = models.CharField(max_length=14)
    testappl = models.CharField(max_length=12)
    testappl_date = models.DateField()
    testcont = models.CharField(max_length=12)
    testcontno = models.CharField(max_length=11)
    testcontmail = models.CharField(max_length=50)
    testtype = models.CharField(max_length=10)
    teststart_date = models.DateField()
    testend_date = models.DateField()
    teststatus = models.CharField(max_length=2)
    agencyno = models.ForeignKey("AgencyInfo",on_delete=models.CASCADE)

    def __str__(self):
        return self.testno