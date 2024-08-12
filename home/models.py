from django.db import models
from django_jalali.db import models as jalali_models
from account.models import Profile
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.


class Register_Time_Enter(models.Model) :

    STATUS_CHOICES = ('login', 'ورود' ) , ('Exit' , 'خروج')

    person_user = models.ForeignKey(Profile , related_name='time_enter_exit' , verbose_name= 'کارمند مورد نظر' , on_delete = models.SET_NULL, null = True  )
    date = jalali_models.jDateTimeField(verbose_name='تاریخ ثبت' , default=timezone.now  )
    status = models.CharField(max_length=15 , verbose_name='وضعیت' , choices= STATUS_CHOICES , default='Login' )
    description = RichTextField(verbose_name= 'توضیحات ' , null = True , blank = True )



    def get_absolute_url(self):
        return reverse('home:detail_record' , args=[str(self.id)])

    def __str__(self) :
        return self.person_user.person.username


    class Meta :
        db_table = 'register_time_enter'
        verbose_name_plural = 'ورود و خروج کارمندان'



