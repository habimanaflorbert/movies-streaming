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
   return render(request,'../templates/abakozi/home.html')

def addcat(request):
   return render(request,'../templates/abakozi/categ.html')

def logout(request):
    auth.logout(request)
    return redirect('/')