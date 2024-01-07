from django.urls import path
from .views import  *

app_name = "main"
urlpatterns = [
    
    path('',main_page, name='main_page'),
    path('about-us',about_page, name='about_page'),
    path('contact',contact_page, name='contact_page'),


]
