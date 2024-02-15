from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
   path('',views.home, name='home'),
   path('login/',views.login , name='login'),
   path('signup/',views.signup),

]

