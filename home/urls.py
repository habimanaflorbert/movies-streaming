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
      path('logout',views.logout,name="logout"),
]