from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from basic_app.models import User,UserDetail
from user_admin.models import UserAdmin,Challenges,AppliedChallenges
from idil import settings
import os
import cv2
# Create your views here.
@login_required
def index(request,username):
    context={}
    print(username+'sjh')
    user_list=User.objects.all()
    challenges=Challenges.objects.all()
    context['challenges']=challenges
    for u in user_list:
        if str(u)==str(username):
            user_info=u
            context['usr']=user_info
            user_admin_list=UserAdmin.objects.all()
            for user2 in user_admin_list:
               if str(user2)==str(username):
                   context['uad']=user2
    return render(request,'user_admin/index.html',context)

@login_required
def acc(request,username):
    user_list=User.objects.all()
    context={}
    for u in user_list:
        if str(u)==str(username):
            user_info=u
            context['usr']=user_info
            user_admin_list=UserAdmin.objects.all()
            for user2 in user_admin_list:
               if str(user2)==str(username):
                   context['uad']=user2
    return render(request,'user_admin/acc.html',context)

@login_required
def upload(request,username):
    user_list=User.objects.all()
    context={}
    for u in user_list:
        if str(u)==str(username):
            user_info=u
            context['usr']=user_info
            user_admin_list=UserAdmin.objects.all()
            for user2 in user_admin_list:
               if str(user2)==str(username):
                   context['uad']=user2
    if request.method=="POST":
        if len(request.FILES)!=0:
           img = request.FILES['pic']
           img_extension = os.path.splitext(img.name)[1]
           s=settings.MEDIA_ROOT
           s=os.path.join(s, 'profile_pics')
           if context['uad'].profile_pic:
                c=str(context['uad'].profile_pic).split("/")[1]
                k=os.path.join(s,c)
                print("ghxc")
                if os.path.exists(k):
                    os.remove(k)
                    context['uad'].profile_pic=request.FILES['pic']
                    context['uad'].save()
                    return render(request,'user_admin/acc.html',context)
           else:
                print("Image not there")
                context['uad'].profile_pic=request.FILES['pic']
                context['uad'].save()
    return render(request,'user_admin/acc.html',context)
@login_required
def save(request,username):
    user_list=User.objects.all()
    context={}
    for u in user_list:
        if str(u)==str(username):
            user_info=u
            context['usr']=user_info
            user_admin_list=UserAdmin.objects.all()
            for user2 in user_admin_list:
               if str(user2)==str(username):
                   context['uad']=user2
    if request.method=="POST":
        context['usr'].email=request.POST.get('email')
        context['usr'].save()
    return render(request,'user_admin/acc.html',context)

@login_required
def update(request,username):
    user_list=User.objects.all()
    context={}
    for u in user_list:
        if str(u)==str(username):
            user_info=u
            context['usr']=user_info
            user_admin_list=UserAdmin.objects.all()
            for user2 in user_admin_list:
               if str(user2)==str(username):
                   context['uad']=user2
    if request.method=="POST":
        context['usr'].first_name=request.POST.get('fn')
        context['usr'].last_name=request.POST.get('ln')
        context['usr'].save()
    return render(request,'user_admin/acc.html',context)

@login_required
def change(request,username):
    user_list=User.objects.all()
    context={}
    for u in user_list:
        if str(u)==str(username):
            user_info=u
            context['usr']=user_info
            user_admin_list=UserAdmin.objects.all()
            for user2 in user_admin_list:
               if str(user2)==str(username):
                   context['uad']=user2
    if request.method=="POST":
        user1=authenticate(username=username,password=request.POST.get('op'))
        if user1==None:
            context['er']=True
        else:
            if request.POST.get('op')==request.POST.get('np'):
                context['dm']=True
            else:
                context['usr'].set_password(request.POST.get('np'))
                context['usr'].save()
    return render(request,'user_admin/acc.html',context)

@login_required
def add(request,username):
    user_list=User.objects.all()
    context={}
    for u in user_list:
        if str(u)==str(username):
            user_info=u
            context['usr']=user_info
            user_admin_list=UserAdmin.objects.all()
            for user2 in user_admin_list:
               if str(user2)==str(username):
                   context['uad']=user2
    return render(request,'user_admin/add.html',context)

@login_required
def save_challenge(request,username):
    user_list=User.objects.all()
    context={}
    for u in user_list:
        if str(u)==str(username):
            user_info=u
            context['usr']=user_info
            user_admin_list=UserAdmin.objects.all()
            for user2 in user_admin_list:
               if str(user2)==str(username):
                   context['uad']=user2
    if request.method=="POST":
        challange=Challenges()
        challange.name=request.POST.get('cn')
        challange.technology=request.POST.get('tech')
        challange.account=request.POST.get('acc')
        challange.capability=request.POST.get('cap')
        challange.applicant_status=request.POST.get('astat')
        challange.expiry_date=request.POST.get('edate')
        challange.category=request.POST.get('cat')
        challange.manager=request.POST.get('manager')
        challange.owner=request.POST.get('powner')
        challange.points=request.POST.get('points')
        challange.desc=request.POST.get('desc')
        challange.applicant_status="NOT FILLED"
        challange.save()
    url = reverse('admin', kwargs={'username': username})
    return HttpResponseRedirect(url)

@login_required
def edit(request,username):

    c_name=username.split('_')[1]
    username=username.split("_")[0]
    challenges=Challenges.objects.all()
    context={}
    k=Challenges()
    for c in challenges:
        if str(c)==c_name:
            context['ch']=c
            k=c
    user_list=User.objects.all()
    for u in user_list:
        if str(u)==str(username):
            user_info=u
            context['usr']=user_info
            user_admin_list=UserAdmin.objects.all()
            for user2 in user_admin_list:
               if str(user2)==str(username):
                   context['uad']=user2
    if request.method=="POST":
         c = Challenges.objects.get(name=k.name)
         print("ed"+c.name)
         c.name=request.POST.get('cn')
         c.technology=request.POST.get('tech')
         c.account=request.POST.get('acc')
         c.capability=request.POST.get('cap')
         c.applicant_status=request.POST.get('astat')
         c.expiry_date=request.POST.get('edate')
         c.category=request.POST.get('cat')
         c.manager=request.POST.get('manager')
         c.owner=request.POST.get('powner')
         c.points=request.POST.get('points')
         c.desc=request.POST.get('desc')
         c.date_posted=k.date_posted
         c.applicant=request.POST.get('applicant')
         c.save()
         url = reverse('admin', kwargs={'username': username})
         return HttpResponseRedirect(url)
    return render(request,'user_admin/edit.html',context)


def delete(request,username):
    c_name=username.split('_')[1]
    username=username.split("_")[0]
    challenges=Challenges.objects.all()
    for c in challenges:
        if str(c)==c_name:
            c.delete()
    url = reverse('admin', kwargs={'username': username})
    return HttpResponseRedirect(url)

@login_required
def show(request,username):
    c_name=username.split('_')[1]
    print(c_name)
    username=username.split("_")[0]
    challenges=Challenges.objects.all()
    context={}
    for c in challenges:
        if str(c)==c_name:
           context['ch']=c
    user_list=User.objects.all()
    for u in user_list:
        if str(u)==str(username):
            user_info=u
            context['usr']=user_info
            user_admin_list=UserAdmin.objects.all()
            for user2 in user_admin_list:
               if str(user2)==str(username):
                   context['uad']=user2
    return render(request,'user_admin/show.html',context)
@login_required
def user_logout(request):
    #request.session.flush()
    logout(request)
    return redirect('/')

@login_required
def applicants(request,username):
    c_name=username.split('_')[1]
    username=username.split("_")[0]
    challenges=Challenges.objects.all()
    context={}
    for c in challenges:
        if str(c)==c_name:
           context['ch']=c
           break
    user_list=User.objects.all()
    for u in user_list:
        if str(u)==str(username):
            user_info=u
            context['usr']=user_info
            user_admin_list=UserAdmin.objects.all()
            for user2 in user_admin_list:
               if str(user2)==str(username):
                   context['uad']=user2
                   break
    appl=AppliedChallenges.objects.filter(challenge=str(context['ch']))
    context['appls']=appl
    for a in appl:
        o=User.objects.filter(username=a.user)
    context['o']=o
    h=[]
    e=dict()
    for i in o:
        a=AppliedChallenges.objects.filter(challenge=str(context['ch'])).filter(user=i.username)
        for r in a:
           e[i.username]=r.completed
    print(e[i.username])
    context['e']=e
    return render(request,'user_admin/applicants.html',context)


@login_required
def complete(request,username):
    c_name=username.split('_')[1]
    print(c_name)
    username=username.split("_")[0]
    challenges=Challenges.objects.all()
    context={}
    for c in challenges:
        if str(c)==c_name:
           context['ch']=c
           break
    user_list=User.objects.all()
    for u in user_list:
        if str(u)==str(username):
            user_info=u
            context['usr']=user_info
            user_admin_list=UserAdmin.objects.all()
            for user2 in user_admin_list:
               if str(user2)==str(username):
                   context['uad']=user2
                   break