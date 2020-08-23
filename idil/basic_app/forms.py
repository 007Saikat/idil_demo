from django import forms
from django.contrib.auth.models import User
from .models import UserDetail

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password*','class':"form-control"}))
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter username*','class':"form-control"}))
    first_name = forms.CharField(max_length=75, required=True,widget= forms.TextInput(attrs={'placeholder':'Enter your first name*','class': "form-control"}))
    last_name=forms.CharField(max_length=75,required=False,widget= forms.TextInput(attrs={'placeholder':'Enter your Last name','class': "form-control"}))
    email = forms.CharField(max_length=75, required=True,widget= forms.TextInput(attrs={'placeholder':'Enter email address*','class': "form-control"}))
    class Meta():
        model=User
        fields=('username','first_name','last_name','email','password')
       

class UserDetailForm(forms.ModelForm):
    profile_pic=forms.ImageField(required=False)
    class Meta():
        model=UserDetail
        fields=('profile_pic',)