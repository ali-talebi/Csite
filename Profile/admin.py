from django.contrib import admin
from .models import AccountInformation
# Register your models here.



@admin.register(AccountInformation)
class AccountInformationAdmin(admin.ModelAdmin):
    list_display = ('show_email', 'money' , 'status' )


    def show_email(self, obj):
        return obj.person.email

    show_email.short_description = 'ایمیل کاربری'