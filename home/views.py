from django.shortcuts import render
import random
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.signing import Signer
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from datetime import date
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
# Create your views here.

def index(request):
   return render(request,'index.html')

def about(request):
   return render(request,'about.html')

def contact(request):
   return render(request,'contact.html')

def signup(request):
       return render(request,'singup.html')

def login(request):
   return render(request,'login.html')

def dashlogin(request):
   if request.method=='POST':
      userd=request.POST['username']
      password=request.POST['pass']
      user=auth.authenticate(username=userd,password=password)
      print(user,"here")
      if user is not None:
         auth.login(request,user)
         person=Admin.objects.get(user=request.user.id)
         
         if person.TypeAccount== "Adin":
            return redirect('dashhome')
         
      messages.info(request,'Login Failed Please Fill Correct Credentals')
      return redirect('dashlogin')
  
   return render(request,'../templates/abakozi/index.html')

def dashhome(request):
   ck=Admin.objects.filter(user=request.user)
   if ck is not None:
      categ=Category.objects.all()
      return render(request,'../templates/abakozi/home.html',{'categ':categ})
   return redirect('/')

def addcat(request):
   ck=Admin.objects.filter(user=request.user)
   if ck is not None:
      categ=Category.objects.all()
      catego=Category.objects.all().order_by('-id')
      if request.method=='POST':
         cate=request.POST['cat']  
         if Category.objects.filter(title=cate).exists():
            msger="Already in please choose another"
            return render(request,'../templates/abakozi/addcat.html',{'msger':msger,'categ':categ,'catego':catego})
         else:
            Category.objects.create(title=cate)
            msg="added Sucessfull"
            return render(request,'../templates/abakozi/addcat.html',{'msg':msg,'categ':categ,'catego':catego})
      return render(request,'../templates/abakozi/addcat.html',{'categ':categ,'catego':catego})
   return redirect('/')


def editcateg(request,pk):
   ck=Admin.objects.filter(user=request.user)
   
   if ck is not None:
      categ=Category.objects.all()
      catego=Category.objects.get(id=pk)
 
      if request.method=='POST':
         cate=request.POST['cat']  
         if Category.objects.filter(title=cate).exists():
            msger="Already in please choose another"
            return render(request,'../templates/abakozi/editcateg.html',{'msger':msger,'categ':categ,'catego':catego})
         else:
            catego.title=cate
            catego.save()

            msg="added Sucessfull"
            return render(request,'../templates/abakozi/editcateg.html',{'msg':msg,'categ':categ,'catego':catego})
      return render(request,'../templates/abakozi/editcateg.html',{'categ':categ,'catego':catego})
   return redirect('/')

def delcateg(request,pk):
   ck=Admin.objects.filter(user=request.user)
   if ck is not None:
      catego=Category.objects.get(id=pk)
      catego.delete()
      return redirect('addcat')
   return redirect('/')


def addmov(request):
   ck=Admin.objects.filter(user=request.user)
   if ck is not None:
      categ=Category.objects.all()
      vd=Videos.objects.all().order_by('-id')
      if request.method=='POST':
         title=request.POST['title']
         desc=request.POST['desc']
         image=request.FILES['image']
         link=request.POST['link']
         category=request.POST['category']
         ct=Category.objects.get(id=int(category))
         
         if Videos.objects.filter(title=title).exists():
            msger="Already in please choose another"
            return render(request,'../templates/abakozi/section.html',{'categ':categ,'msger':msger,'vd':vd})
         else:
            Videos.objects.create(title=title,desc=desc,image=image,category=link,categ=ct)
            msg="added Sucessfull"
            return render(request,'../templates/abakozi/section.html',{'categ':categ,'msg':msg,'vd':vd})
      return render(request,'../templates/abakozi/section.html',{'categ':categ,'vd':vd})
   return redirect('/')

def editmov(request,pk):
   ck=Admin.objects.filter(user=request.user)
   if ck is not None:
      categ=Category.objects.all()
      vd=Videos.objects.get(id=pk)
      if request.method=='POST':
         title=request.POST['title']
         desc=request.POST['desc']
         link=request.POST['link']
         category=request.POST['category']
         ct=Category.objects.get(id=int(category))
         vd.title=title
         vd.desc=desc
         vd.category=link
         vd.categ=ctvd.save()
         msg="added Sucessfull"
         return render(request,'../templates/abakozi/editmov.html',{'categ':categ,'msg':msg,'vd':vd})
      return render(request,'../templates/abakozi/editmov.html',{'categ':categ,'vd':vd})
   return redirect('/')






def logout(request):
    auth.logout(request)
    return redirect('/')