from django.contrib import admin
from django.urls import path
from naseem import views


urlpatterns = [
    path('',views.index,name="home"),
    path('index.html',views.index,name="home"),
    path('services.html',views.services,name="service"),
    path('events.html',views.events,name="events"),
    path('about.html',views.about,name="about"),
    path('contact.html',views.contact,name="contact"),
    path('login.html',views.login,name="login"),
    path('register.html',views.register,name="register"),
    path('logout',views.logout,name="register"),
    path('delhi',views.delhi,name="delhi"),

]