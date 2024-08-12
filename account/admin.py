from django.contrib import admin
from .models import Profile
from django.utils.html import format_html
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('person' , 'phone' , 'show_img' )


    def show_img(self , obj ) :
        return format_html('<img width=50px height=50px src="{}">'.format(obj.picture.url))

    show_img.short_description = 'تصویر کاربری'

