from django.shortcuts import render,redirect
from .forms import UserForm,UserDetailForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from .models import User,UserDetail
from user_admin.models import UserAdmin,Challenges,AppliedChallenges
from idil import settings
import os
import cv2
# Create your views here.
@login_required
def home(request,username):
    context={}
    print(username+'sjh')
    user_list=User.objects.all()
    challenges=Challenges.objects.all()
    ac=AppliedChallenges.objects.all()
    context['challenges']=challenges
    appl=True
    p=0
    for u in user_list:
        if str(u)==str(username):
            user_info=u
            context['usr']=user_info
            users=UserDetail.objects.all()
            for user2 in users:
               if str(user2)==str(username):
                   context['usd']=user2
    for c in challenges:
        for a in ac:
            if str(a.challenge)==str(c.name) and str(a.user)==str(context['usr']):
                p=a.points
                appl=False
                break
    context['a']=appl
    context['p']=p
    return render(request,'basic_app/home.html',context)

@login_required
def acc(request,username):
    user_list=User.objects.all()
    context={}
    for u in user_list:
        if str(u)==str(username):
            user_info=u
            context['usr']=user_info
            user_detail_list=UserDetail.objects.all()
            for user2 in user_detail_list:
               if str(user2)==str(username):
                   context['usd']=user2
    return render(request,'basic_app/acc.html',context)


@login_required
def upload(request,username):
    user_list=User.objects.all()
    context={}
    for u in user_list:
        if str(u)==str(username):
            user_info=u
            context['usr']=user_info
            user_details_list=UserDetail.objects.all()
            for user2 in user_details_list:
               if str(user2)==str(username):
                   context['usd']=user2
    if request.method=="POST":
        if len(request.FILES)!=0:
           img = request.FILES['pic']
           img_extension = os.path.splitext(img.name)[1]
           s=settings.MEDIA_ROOT
           s=os.path.join(s, 'profile_pics')
           if context['usd'].profile_pic:
                c=str(context['usd'].profile_pic).split("/")[1]
                k=os.path.join(s,c)
                print("ghxc")
                if os.path.exists(k):
                    os.remove(k)
                    context['usd'].profile_pic=request.FILES['pic']
                    context['usd'].save()
                    return render(request,'basic_app/acc.html',context)
           else:
                print("Image not there")
                context['usd'].profile_pic=request.FILES['pic']
                context['usd'].save()
    return render(request,'basic_app/acc.html',context)
@login_required
def save(request,username):
    user_list=User.objects.all()
    context={}
    for u in user_list:
        if str(u)==str(username):
            user_info=u
            context['usr']=user_info
            user_detail_list=UserDetail.objects.all()
            for user2 in user_detail_list:
               if str(user2)==str(username):
                   context['usd']=user2
    if request.method=="POST":
        context['usr'].email=request.POST.get('email')
        context['usr'].save()
    return render(request,'basic_app/acc.html',context)

@login_required
def update(request,username):
    user_list=User.objects.all()
    context={}
    for u in user_list:
        if str(u)==str(username):
            user_info=u
            context['usr']=user_info
            user_detail_list=UserDetail.objects.all()
            for user2 in user_detail_list:
               if str(user2)==str(username):
                   context['usd']=user2
    if request.method=="POST":
        context['usr'].first_name=request.POST.get('fn')
        context['usr'].last_name=request.POST.get('ln')
        context['usr'].save()
    return render(request,'basic_app/acc.html',context)

@login_required
def change(request,username):
    user_list=User.objects.all()
    context={}
    for u in user_list:
        if str(u)==str(username):
            user_info=u
            context['usr']=user_info
            user_detail_list=UserDetail.objects.all()
            for user2 in user_detail_list:
               if str(user2)==str(username):
                   context['usd']=user2
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
    return render(request,'basic_app/acc.html',context)


@login_required
def user_logout(request):
    #request.session.flush()
    logout(request)
    return redirect('/')

def index(request):
    context={}
    context['name']='Saikat'
    # user_form=UserForm(data=request.POST)
    # user_detail_form=UserDetailForm(data=request.POST)
    # context['user_form']=user_form
    # context['user_detail_form']=user_detail_form
    return render(request,'basic_app/index.html',context)

def login_register(request):
    show_div=False
    print(request.method)
    if request.GET.get('login'):
        show_div=False
    elif request.GET.get('reg'):
        show_div=True
    context={}
    context['error']=False
    user_form=UserForm(data=request.POST)
    user_detail_form=UserDetailForm(data=request.POST)
    user_detail1=UserDetail
    if request.method == "POST" and show_div:
        print(user_form.is_valid())
        print(user_detail_form.is_valid())
        if user_form.is_valid() and user_detail_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user_detail=user_detail_form.save(commit=False)
            user_detail.user=user
            if len(request.FILES)!=0:
                p=request.FILES['profile_pic']
                p=str(p)
                print(p)
                if p.endswith('.jpg') or p.endswith('.jpeg') or p.endswith('.png'):
                    user_detail.profile_pic=request.FILES['profile_pic']
                    user.save()
                    user_detail.save()
                    request.session['username']=user.username
                    login(request,user)
                    return redirect('/basic_app/home')
                else:
                    context['show_div']=True
                    context['user_form']=user_form
                    context['user_detail_form']=user_detail_form
                    context['warning']=True
                    return render(request,'basic_app/login.html',context)
            else:
                user.save()
                user_detail.save()
                request.session['username']=user.username
                login(request,user)
                return redirect('/basic_app/home')
           
    elif request.method == "POST" and not show_div:
       username=request.POST.get('username')
       password=request.POST.get('password')
       user1=authenticate(username=username,password=password)

       if user1!=None:
           user_detail_list=UserDetail.objects.all()
           ef=False
           for user2 in user_detail_list:
               if str(user2)==str(user1):
                   ef=True
                   break
           user_admin_list=UserAdmin.objects.all()
           af=False
           for user2 in user_admin_list:
               if str(user2)==str(user1):
                   print(user2)
                   af=True
                   break
           request.session['username']=user1.username
           if af:
             u=str(user1)
             url = reverse('admin', kwargs={'username': u})
             print(url)
             login(request,user1)
             return HttpResponseRedirect(url)
           elif ef:
                u=str(user1)
                url = reverse('user', kwargs={'username': u})
                login(request,user1)
                return HttpResponseRedirect(url)
       else:                                                                         
           context['error']=True
    context['user_form']=user_form
    context['user_detail_form']=user_detail_form
    context['show_div']=show_div
    return render(request,'basic_app/login.html',context)

@login_required
def show(request,username):
    c_name=username.split('_')[1]
    print(c_name)
    username=username.split("_")[0]
    challenges=Challenges.objects.all()
    ac=AppliedChallenges.objects.all()
    appl=True
    context={}
    for c in challenges:
        if str(c)==c_name:
           context['ch']=c
    user_list=User.objects.all()
    for u in user_list:
        if str(u)==str(username):
            user_info=u
            context['usr']=user_info
            user_detail_list=UserDetail.objects.all()
            for user2 in user_detail_list:
               if str(user2)==str(username):
                   context['usd']=user2
    for a in ac:
        if str(a.challenge)==str(context['ch']) and str(a.user)==str(context['usr']):
            appl=False
            break
    context['a']=appl
    return render(request,'basic_app/show.html',context)
 
@login_required
def apply(request,username):
    print(username)
    u=username.split("_")[0]
    c=username.split("_")[1]
    a=AppliedChallenges()
    n=0
    challenges=Challenges.objects.all()
    for ca in challenges:
        if str(ca.name)==c:
            n=ca.applicant
            break
    n=n+1
    l=AppliedChallenges.objects.filter(user=u).filter(challenge=c)
    if(len(l)==0):
        Challenges.objects.filter(pk=c).update(applicant=n)
        a.user=u
        a.challenge=c
        a.save()
    url = reverse('user', kwargs={'username': u})
    return HttpResponseRedirect(url)