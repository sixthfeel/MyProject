from django.contrib import admin
from .models import *

# Register your models here.


class AgencyInfoAdmin(admin.ModelAdmin):
    list_display = [
        'agencyno', 'agencyname', 'agencytype', 'agencyonprd'
    ]
    list_filter = ['agencyno', 'agencyonprd']
    search_fields = ['agencyno']
    list_per_page = 5


class TestInfoAdmin(admin.ModelAdmin):
    list_display = [
        'testno', 'testappl', 'testappldate', 'testcont', 'testcontno',
        'testcontmail', 'testtype', 'teststartdate', 'testenddate',
        'teststatus', 'agencyno'
    ]


admin.site.register(AgencyInfo, AgencyInfoAdmin)
admin.site.register(TestInfo, TestInfoAdmin)
