from django.urls import path
from .views import  *

app_name = "main"
urlpatterns = [
    
    path('',main_page, name='main_page'),
    path('blogs',blogs_page, name='blogs_page'),


]
