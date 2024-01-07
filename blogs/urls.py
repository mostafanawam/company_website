from django.urls import path
from .views import  *

app_name = "blogs"
urlpatterns = [
    
    path('',blogs_page, name='blogs_page'),
    path('<int:pk>',blog_details, name='blog_details'),



]
