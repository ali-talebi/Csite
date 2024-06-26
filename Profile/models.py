from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class AccountInformation(models.Model) :
    person = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name= "جساب کاربری" )
    money  = models.FloatField(default=0 , verbose_name= "میزان اعتبار"  )
    phone  = models.CharField(max_length=11 , verbose_name= "شماره تلفن" , unique= True , default='0')
    status = models.BooleanField(verbose_name= "وضعیت حساب کاربری" , default=False )




    def __str__(self):
        return self.person.email


    class Meta:
        db_table = 'accountinformation'
        verbose_name_plural = 'اطلاعات حساب کاربری'