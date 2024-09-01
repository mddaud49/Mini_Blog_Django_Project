from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post

class SignForm(UserCreationForm):
    password2=forms.CharField(label='confirm password (again)',widget=forms.PasswordInput)
    usable_password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','disc']