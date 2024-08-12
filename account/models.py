from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    person  = models.OneToOneField(User , verbose_name='کارمند' , on_delete=models.CASCADE )
    phone   = models.CharField(max_length=11 , verbose_name= 'شماره تماس' , blank = True , null = True )
    picture = models.FileField(verbose_name='تصویر کاربری' , upload_to='Profile_pics' )


    def __str__(self):
        return self.person.username


    class Meta :
        db_table = 'profile'
        verbose_name_plural = 'حساب کاربری کارمندان'
