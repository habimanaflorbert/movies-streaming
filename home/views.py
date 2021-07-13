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
   if request.method=='POST':
      fname=request.POST['fname'] 
      lname=request.POST['lname']
      username=request.POST['username']
      dob=request.POST['dob']
      pass1=request.POST['pass1']
      pass2=request.POST['pass2']
      if pass1 == pass2:
         if User.objects.filter(email=username).exists():
            messages.info(request,'Email is already exist taken')
            return redirect('signup')
         else:
            user=User.objects.create_user(first_name=fname,last_name=lname,email=username,username=username,password=pass1)
            user.save()
            Clients.objects.create(TypeAccount='Client',user=user,age=dob).save()
            msg="We have been created account please login"
            return render(request,'singup.html',{'msg':msg})
      else:
         messages.info(request,'Password Not Match')
         return redirect('signup')
         
   return render(request,'singup.html')

def login(request):
   if request.method=='POST':
      userd=request.POST['username']
      password=request.POST['pass']
      user=auth.authenticate(username=userd,password=password)
      print(user,"here")
      if user is not None:
         auth.login(request,user)
         person=Clients.objects.get(user=request.user.id)
         
         if person.TypeAccount== "Client":
            return redirect('home')
         
      messages.info(request,'Login Failed Please Fill Correct Credentals')
      return redirect('login')
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
         
         if person.TypeAccount== "Admin":
            return redirect('dashhome')
         
      messages.info(request,'Login Failed Please Fill Correct Credentals')
      return redirect('dashlogin')
  
   return render(request,'../templates/abakozi/index.html')

def dashhome(request):
   ck=Admin.objects.filter(user=request.user)
   if ck is not None:
      categ=Category.objects.all()
      users=User.objects.all().count()
      movies=Videos.objects.all().count()
      per=users*100/movies
      return render(request,'../templates/abakozi/home.html',{'categ':categ,'users':users,'per':per,'movies':movies})
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
         if Videos.objects.filter(title=title).exists():
            msger="Already in please choose another"
            return render(request,'../templates/abakozi/editmov.html',{'categ':categ,'msger':msger,'vd':vd})
         else:
            vd.title=title
            vd.desc=desc
            vd.category=link
            vd.categ=ct
            vd.save()
            msg="added Sucessfull"
            return render(request,'../templates/abakozi/editmov.html',{'categ':categ,'msg':msg,'vd':vd})
      return render(request,'../templates/abakozi/editmov.html',{'categ':categ,'vd':vd})
   return redirect('/')

def editmovcov(request,pk):
   ck=Admin.objects.filter(user=request.user)
   if ck is not None:
      categ=Category.objects.all()
      vd=Videos.objects.get(id=pk)
      if request.method=='POST':
         image=request.FILES['image']
         vd.image=image
         vd.save()
         msg="added Sucessfull"
         return render(request,'../templates/abakozi/editmov.html',{'categ':categ,'msg':msg,'vd':vd})
      return render(request,'../templates/abakozi/editmov.html',{'categ':categ,'vd':vd})
   return redirect('/')

def delmov(request,pk):
   ck=Admin.objects.filter(user=request.user)
   if ck is not None:
      catego=Videos.objects.get(id=pk)
      catego.delete()
      return redirect('addmov')
   return redirect('/')

def movies(request,slug):
   ck=Admin.objects.filter(user=request.user)
   if ck is not None:
      categ=Category.objects.all()
      cat=Category.objects.get(slug=slug)
      nin=cat.title
      mov=Videos.objects.filter(categ=cat)
      return render(request,'../templates/abakozi/movies.html',{'categ':categ,'mov':mov,'nin':nin})
   return redirect('/')

def allmv(request):
   ck=Admin.objects.filter(user=request.user)
   if ck is not None:
      categ=Category.objects.all()
      mov=Videos.objects.all()
      return render(request,'../templates/abakozi/all.html',{'categ':categ,'mov':mov})
   return redirect('/')


def moreview(request,slug):
   ck=Admin.objects.filter(user=request.user)
   if ck is not None:
      categ=Category.objects.all()
      dt=Videos.objects.get(slug=slug)
      return render(request,'../templates/abakozi/view.html',{'categ':categ,'dt':dt})
   return redirect('/')

def vwm(request,id):
   ck=Admin.objects.filter(user=request.user)
   if ck is not None:
      categ=Category.objects.all()
      dt=Videos.objects.get(id=id)
      return render(request,'../templates/abakozi/play.html',{'categ':categ,'dt':dt})
   return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/')

def home(request):
   if str(request.user) == 'AnonymousUser':
      return redirect('/') 
   else:
      categ=Category.objects.all()
      mov=Videos.objects.all()
      return render(request,"../templates/clients/home.html",{'categ':categ,'mov':mov})

def clientmovies(request,slug):
   if str(request.user) == 'AnonymousUser':
      return redirect('/') 
   else:
      categ=Category.objects.all()
      cat=Category.objects.get(slug=slug)
      nin=cat.title
      mov=Videos.objects.filter(categ=cat)
      return render(request,'../templates/clients/movies.html',{'categ':categ,'mov':mov,'nin':nin})

def moreviewclient(request,slug):
   if str(request.user) == 'AnonymousUser':
      return redirect('/') 
   else:
      categ=Category.objects.all()
      dt=Videos.objects.get(slug=slug)
      return render(request,'../templates/clients/view.html',{'categ':categ,'dt':dt})

def vwmclient(request,slug):
   if str(request.user) == 'AnonymousUser':
      return redirect('/') 
   else:
      categ=Category.objects.all()
      dt=Videos.objects.get(slug=slug)
      return render(request,'../templates/clients/play.html',{'categ':categ,'dt':dt})

# def editaccountpass(request):
#    if str(request.user) != 'AnonymousUser':
#       if request.method =='POST':
#          cpass=request.POST['pass1']
#          npass=request.POST['pass2']
#          newpass=make_password(npass)
#          dt=User.objects.get(username=request.user)
#          cpassword=dt.password
#          if check_password(cpass,cpassword) ==True:
#                dt.password=newpass
#                dt.save()
#                auth.logout(request)
#                return redirect('login')
#          else:
#                msgerror='please enter correct password'
#                return render(request,'person/password.html',{'msgerror':msgerror})
#       return render(request,'person/password.html')

#    else:
#       return redirect('/')