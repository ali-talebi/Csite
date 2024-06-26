from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import AccountInformation



@receiver(post_save, sender=User)
def create_profile(sender , **kwargs):
    if kwargs['created']:
        AccountInformation.objects.create(user=kwargs['instance'])


#post_save.connect(receiver=create_profile, sender=User)
