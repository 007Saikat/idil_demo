from django.db import models
from django.contrib.auth.models import User
import os
from uuid import uuid4
import datetime

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
def o():
    return "NOT FILLED"
class UserAdmin(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    role=models.CharField(max_length=128,default='admin')
    profile_pic=models.ImageField(upload_to=path_and_rename,blank=True,null=True)
    last_login = models.DateTimeField(blank=True,null=True)
    def __str__(self):
        return self.user.username
        
class Challenges(models.Model):
    name=models.CharField(primary_key=True,max_length=255)
    technology=models.CharField(max_length=255)
    account=models.CharField(max_length=255)
    capability=models.CharField(max_length=255)
    applicant_status=models.CharField(max_length=255,default="NOT FILLED")
    date_posted=models.DateField(default=datetime.date.today)
    expiry_date=models.DateField()
    applicant=models.IntegerField(default=0)
    manager=models.CharField(max_length=255)
    owner=models.CharField(max_length=255)
    desc=models.CharField(max_length=255)
    points=models.IntegerField()
    category=models.CharField(max_length=255)

    def __str__(self):
        return self.name
class AppliedChallenges(models.Model):
    user=models.CharField(max_length=255)
    challenge=models.CharField(max_length=255)
    completed=models.BooleanField(default=False)
    points=models.IntegerField(default=0)

    def __str__(self):
        return self.user+'_'+self.challenge