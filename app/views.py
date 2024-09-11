from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group
from .forms import SignForm,PostForm
from .models import Post
# from django.core.cache import cache
# Create your views here.
def Home(request):
    posts=Post.objects.all()
    return render(request,'home.html',{'posts':posts})

def About(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')

def Dashboard(request):
    if request.user.is_authenticated:
     posts=Post.objects.all()
     user=request.user
     full_name = user.get_full_name()
     gps=user.groups.all()
     ip=request.session.get('ip',0)
   #   ct=cache.get('count',version=user.pk)
     return render(request,'dashboard.html',{'posts':posts,'full_name':full_name,'groups':gps,
                                             'ip':ip,})
    else:
       return HttpResponseRedirect('/login/')

def Signup(request):
    if request.method=='POST':
        fm=SignForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Congrat You Become An Author ')
            user=fm.save()
            group=Group.objects.get(name='author')
            user.groups.add(group)
    else:
     fm=SignForm()
    return render(request,'signup.html',{'form':fm})


def Login(request):
  if not request.user.is_authenticated:
    if request.method=='POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            unm=fm.cleaned_data['username']
            ups=fm.cleaned_data['password']
            user=authenticate(username=unm,password=ups)
            if user is not None:
                login(request,user)
                messages.success(request,'login successfull')
                return HttpResponseRedirect('/dashboard/')
    else:
     fm=AuthenticationForm(request=request)
    return render(request,'login.html',{'form':fm})
  else:
     return HttpResponseRedirect('/dashboard/')
 

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def Delete(request,id):
 if request.user.is_authenticated:
   pi=Post.objects.get(pk=id)
   pi.delete()
   return  HttpResponseRedirect('/dashboard/')
 else:
    return  HttpResponseRedirect('/login/')
 


def AddPost(request):
   if request.user.is_authenticated:
      if request.method=='POST':
         form=PostForm(request.POST)
         if form.is_valid():
            title=form.cleaned_data['title']
            disc=form.cleaned_data['disc']
            post=Post(title=title,disc=disc)
            post.save()
            messages.success(request,'added succeefully')
            form=PostForm()
      else:
         form=PostForm()
      return render(request,'addpost.html',{'form':form})
   else:
      return HttpResponseRedirect('/login/')

def Update(request,id):
   if request.user.is_authenticated:
      if request.method=='POST':
         pi=Post.objects.get(pk=id)
         form=PostForm(request.POST,instance=pi)
         if form.is_valid():
            form.save()
            messages.success(request,'Updated succeefully')
        
            
      else:
         pi=Post.objects.get(pk=id)
         form=PostForm(instance=pi)
      return render(request,'update.html',{'form':form})
   else:
      return HttpResponseRedirect('/login/')
    
   

