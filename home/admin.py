from django.contrib import admin
from .models import Register_Time_Enter
# Register your models here.



@admin.register(Register_Time_Enter)
class Register_Time_Enter_Admin(admin.ModelAdmin):
    list_display = ('person_user' , 'show_date' , 'status' )
    list_editable = ('status' ,  )
    list_filter = ('person_user' , 'date' )


    def show_date(self , obj ) :
        return obj.date.strftime('%m/%d/%Y | %S - %M - %H ')

    show_date.short_description = 'زمان ورود یا خروج'
