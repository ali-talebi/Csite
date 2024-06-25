from django.db import models
from django_jalali.db import models as jalali_models
from django.urls import reverse
# Create your models here.



class Search_Domain(models.Model) :

    search_level_status = (
        ('1' , 'جستجوی سطح ۱ ') ,
        ('2' , 'جستجوی سطح ۲ ') ,
    )

    domain_name = models.CharField(max_length=150 , verbose_name="آدرس دامنه" )
    total_text  = models.TextField(verbose_name="متن موجود در صفحه" , null = True , blank = True )
    total_link  = models.TextField(verbose_name="دامنه های موجود"   , null = True , blank = True )
    server      = models.CharField(verbose_name="سرور" , max_length=100 , null = True , blank = True )
    status      = models.CharField(verbose_name= "وضعیت درخواست"  , max_length=100 )
    time        = jalali_models.jDateTimeField(verbose_name="تاریخ درخواست" , null = True , blank = True , auto_now=True  )
    serch_level = models.CharField(max_length =1 , verbose_name=  'سطح جستجوی' , null = True , blank = True )
    summary     = models.TextField(verbose_name="خلاصه متن موجود")
    classify    = models.CharField(verbose_name="دسته بندی" , max_length=100 , null = True , blank = True )

    def __str__(self):
        return self.domain_name



    def get_absolute_url(self):
        return reverse('home:detail', kwargs={'id': self.id})

    class Meta:
        verbose_name_plural = "دامنه های مورد جستحو"
        db_table = 'search_domain'

        ordering = ['-id']


class Guideline(models.Model):
    title = models.CharField(verbose_name="عنوان راهنمایی" , max_length=100 )
    text  = models.TextField(verbose_name="متن راهنمایی")



    def __str__(self):
        return self.title


    class Meta :
        db_table = 'Guideline'
        ordering = ['-id']
        verbose_name_plural = "راهنمایی های وبسایت"