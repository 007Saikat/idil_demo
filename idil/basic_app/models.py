from django.db import models
from django.contrib.auth.models import User
import os
from uuid import uuid4

def path_and_rename(instance, filename):
    upload_to = 'profile_pics'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)
# Create your models here.

class UserDetail(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    role=models.CharField(max_length=128,default='employee')
    profile_pic=models.ImageField(upload_to=path_and_rename,blank=True,null=True)
    last_login = models.DateTimeField(blank=True,null=True)
    def __str__(self):
        return self.user.username