from django.contrib import admin
from .models import *
# Register your models here.


class AgencyInfoAdmin(admin.ModelAdmin):
    list_display = ['agencyno', 'agencyname', 'agencytype']
class TestInfoAdmin(admin.ModelAdmin):
    list_display = ['testno', 'testappl', 'testappl_date', 'testcont', 'testcontno', 'testcontmail', 'testtype',
                    'teststart_date', 'testend_date', 'teststatus', 'agencyno']


admin.site.register(AgencyInfo, AgencyInfoAdmin)
admin.site.register(TestInfo, TestInfoAdmin)