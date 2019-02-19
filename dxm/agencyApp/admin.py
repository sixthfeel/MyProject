from django.contrib import admin
from .models import *
# Register your models here.


class AgencyInfoAdmin(admin.ModelAdmin):
    list_display = ['agencyno', 'agencyname', 'agencytype', 'agencyonprd']


class TestInfoAdmin(admin.ModelAdmin):
    list_display = ['testno', 'testappl', 'testappldate', 'testcont', 'testcontno', 'testcontmail', 'testtype',
                    'teststartdate', 'testenddate', 'teststatus', 'agencyno']


admin.site.register(AgencyInfo, AgencyInfoAdmin)
admin.site.register(TestInfo, TestInfoAdmin)
