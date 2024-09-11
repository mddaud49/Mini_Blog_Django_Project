from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver
# from django.core.cache import cache

@receiver(user_logged_in,sender=User)
def login_successfull(sender,request,user,**kwargs):
    print('login successfull')
    ip=request.META.get('REMOTE_ADDR')
    request.session['ip']=ip
    # ct=cache.get('count',0,version=user.pk)
    # newcount=ct+1
    # cache.set('count',newcount,version=user.pk)



