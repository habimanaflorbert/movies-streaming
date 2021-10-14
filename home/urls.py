from django.urls import path
from .import views
from.views import *

urlpatterns = [
      path('',views.index, name="welcome"),
      path('about-us/',views.about, name="about"),
      path('contact-us/',views.contact, name="contact"),
      path('register-Account',views.signup, name="signup"),
      path('login/',views.login, name="login"),
      path('james/',views.dashlogin, name="dashlogin"),
      path('dashboard-home',views.dashhome, name="dashhome"),
      path('categories',views.addcat,name="addcat"),
      path('categories/<int:pk>/',views.editcateg,name="editcateg"),
      path('category-delete/<int:pk>/',views.delcateg,name="delcateg"),
      #  path('admin/<int:id>/',views.section,name="admin"),
      path('edit-movies/<int:pk>',views.editmov,name="editmov"),
      path('add-movie/',views.addmov,name="addmov"),
      path('Change-cover/<int:pk>',views.editmovcov,name="editmovcov"),
      path('delete-movie/<int:pk>',views.delmov,name="delmov"),
      path('Movies/<slug:slug>',views.movies,name="movies"),
      path('view-detail/<slug:slug>',views.moreview,name="moreview"),
      path('view-movies/<int:id>',views.vwm,name="movieview"),
      path('home-Dash',views.home,name="home"),
      path('logout',views.logout,name="logout"),
      path('all-Movies',views.allmv,name="allmv"),
      path('customer-movies/<slug:slug>',views.clientmovies,name="clientmovies"),
      path('view-detail-client/<slug:slug>',views.moreviewclient,name="moreviewclient"),
      path('view-movies-client/<slug:slug>',views.vwmclient,name="movieviewclient"),

]