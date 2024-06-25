from django.contrib import admin
from .models import Search_Domain , Guideline
# Register your models here.


@admin.register(Search_Domain)
class Search_DomainAdmin(admin.ModelAdmin):
    list_display = ('domain_name' , 'status' , 'serch_level' , 'show_time' , 'server' )

    def show_time(self , obj ) :
        return obj.time.strftime('%Y-%m-%d %H:%M:%S')

    show_time.short_description = 'تاریخ و زمان درخواست'



@admin.register(Guideline)
class GuidelineAdmin(admin.ModelAdmin):
    list_display = ('title' , )

