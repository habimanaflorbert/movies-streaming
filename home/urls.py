from django.urls import path
from .import views
from.views import *

urlpatterns = [
      path('',views.index, name="welcome"),
      path('About-us',views.about, name="about"),
      path('Contact-us',views.contact, name="contact"),
      path('Register-Account',views.signup, name="signup"),
      path('Login',views.login, name="login"),
      path('james',views.dashlogin, name="dashlogin"),
      path('Dashboard-home',views.dashhome, name="dashhome"),
      path('categories',views.addcat,name="addcat"),
      path('categories/<int:pk>/',views.editcateg,name="editcateg"),
      path('category-delete/<int:pk>/',views.delcateg,name="delcateg"),
      #  path('admin/<int:id>/',views.section,name="admin"),
      path('edit-movies/<int:pk>',views.editmov,name="editmov"),
      path('add-movie',views.addmov,name="addmov"),
      path('Change-cover/<int:pk>',views.editmovcov,name="editmovcov"),
      path('delete-movie/<int:pk>',views.delmov,name="delmov"),
      path('Movies/<slug:slug>',views.movies,name="movies"),
      path('logout',views.logout,name="logout"),

]