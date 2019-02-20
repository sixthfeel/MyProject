from django.contrib import admin
from .models import *

# Register your models here.


class AgencyInfoAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ['agencyno', 'agencyname', 'agencytype']
=======
    list_display = [
        'agencyno', 'agencyname', 'agencytype', 'agencyonprd'
    ]
    list_filter = ['agencyno', 'agencyonprd']
    search_fields = ['agencyno']
    list_per_page = 20

>>>>>>> 170c433fa3873583535d1498cf94429a203761a6

class TestInfoAdmin(admin.ModelAdmin):
    list_display = [
        'testno', 'testappl', 'testappldate', 'testcont', 'testcontno',
        'testcontmail', 'testtype', 'teststartdate', 'testenddate',
        'teststatus', 'agencyno'
    ]
    list_filter = ['agencyno', 'teststartdate', 'testenddate']
    ordering = ('-teststartdate',)
    list_per_page = 20


admin.site.register(AgencyInfo, AgencyInfoAdmin)
admin.site.register(TestInfo, TestInfoAdmin)
